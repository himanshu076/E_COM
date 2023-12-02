from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]
        # read_only = []


class ProductListSerializer(serializers.ModelSerializer):
    product_image = serializers.SerializerMethodField()

    # breakpoint()
    def get_product_image(self, product):
        request = self.context.get("request")
        product_images = product.images.all()
        if product_images.exists():
            serializer = ProductImageSerializer(product_images, many=True)
            image_data = serializer.data
            image_urls = [
                request.build_absolute_uri(image["image"]) for image in image_data
            ]
            return image_urls
        return None

    class Meta:
        model = Product
        fields = "__all__"

    # read_only_fields = ['slug', 'created', 'updated']


class ProductCreateSerializer(serializers.ModelSerializer):
    product_image = serializers.ListField(
        child=serializers.ImageField(), allow_empty=True, write_only=True
    )
    images_product = serializers.SerializerMethodField()

    def get_images_product(self, product):
        request = self.context.get("request")
        product_images = product.images.all()
        if product_images.exists():
            serializer = ProductImageSerializer(product_images, many=True)
            image_data = serializer.data
            image_urls = [
                request.build_absolute_uri(image["image"]) for image in image_data
            ]
            return image_urls
        return None

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["slug", "created", "updated", "images_product"]

    def create(self, validated_data):
        product_images_data = validated_data.pop("product_image", [])
        product = super().create(validated_data)

        if product_images_data is not None:
            for image_data in product_images_data:
                new_image = ProductImage.objects.create(image=image_data)
                new_image.product.add(product)
        return product

    # def update(self, instance, validated_data):
    #     store_images_data = validated_data.pop('store_image', [])
    #     instance = super().update(instance, validated_data)

    #     for image_data in store_images_data:
    #         instance_image = ProductImage.objects.filter(store=instance)
    #         if instance_image:
    #             instance_image.delete()
    #         ProductImage.objects.create(store=instance, image=image_data)
    #     return instance
