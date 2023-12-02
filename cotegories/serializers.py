from rest_framework import serializers

from cotegories.models import Category, Store, StoreImage


class ListCategorySerializer(serializers.ModelSerializer):
    # slug = serializers.ModelField(model_field=Category()._meta.get_field('slug'))
    class Meta:
        model = Category
        fields = "__all__"


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description", "parent"]


class MultipleCategorySerializer(serializers.ModelSerializer):
    category_list = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Category
        fields = ["category_list"]


class StoreImageSerializer(serializers.ModelSerializer):
    # store_image = serializers.SerializerMethodField()

    class Meta:
        model = StoreImage
        fields = ["image"]


class StoreSerializer(serializers.ModelSerializer):
    store_image = serializers.ImageField(write_only=True)
    image_store = serializers.SerializerMethodField()

    def get_image_store(self, store):
        request = self.context.get("request")
        store_images = store.store_images.all()
        if store_images.exists():
            serializer = StoreImageSerializer(store_images.first())
            image_data = serializer.data
            image_urls = request.build_absolute_uri(image_data["image"])
            return image_urls
        return None

    class Meta:
        model = Store
        fields = "__all__"
        read_only_fields = ["created", "updated", "image_store"]

    def create(self, validated_data):
        store_images_data = validated_data.pop("store_image", [])
        store = super().create(validated_data)

        if store_images_data is not None:
            StoreImage.objects.create(store=store, image=store_images_data)
            return store

    def update(self, instance, validated_data):
        store_images_data = validated_data.pop("store_image", [])
        instance = super().update(instance, validated_data)

        instance_image = StoreImage.objects.filter(store=instance)
        if instance_image:
            instance_image.delete()
        StoreImage.objects.create(store=instance, image=store_images_data)
        return instance
