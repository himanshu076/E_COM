from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoll(models.TextChoices):
    USER = "U", _("User")
    VENDOR = "O", _("Owner")


class UserDepartment(models.TextChoices):
    SELECT = "", _("Select")
    ADMIN = "ADM", _("Admin")
    HUMAN_RESOURCES = "HR", _("Human Resources")
    ACCOUNT = "ACCT", _("Account")
    IT = "It", _("Information Technology")
    BUSINESS_DEVELOPMENT = "A", _("Business Development")
    MARKETING = "MKTG", _("Marketing")
    SALES = "S", _("Sales")


class Gender(models.TextChoices):
    SELECT = "", _("Select")
    MALE = "ML", _("Male")
    FEMALE = "FL", _("Female")
    TRANSGENDER = "TS", _("Transgender")
    OTHER = "OT", _("Other")


class Country_Phone_Code(models.TextChoices):
    Aruba = "297", _("297")
    Afghanistan = "93", _("93")
    Angola = "244", _("244")
    Anguilla = "1264", _("1264")
    Aland_Islands = "358", _("358")
    Albania = "355", _("355")
    Andorra = "376", _("376")
    United_Arab_Emirates = "971", _("971")
    Argentina = "54", _("54")
    Armenia = "374", _("374")
    American_Samoa = "1684", _("1684")
    Antigua_and_Barbuda = "1268", _("1268")
    Australia = "61", _("61")
    Austria = "43", _("43")
    Azerbaijan = "994", _("994")
    Burundi = "257", _("257")
    Belgium = "32", _("32")
    Benin = "229", _("229")
    Burkina_Faso = "226", _("226")
    Bangladesh = "880", _("880")
    Bulgaria = "359", _("359")
    Bahrain = "973", _("973")
    Bahamas = "1242", _("1242")
    Bosnia_and_Herzegovina = "387", _("387")
    # Saint_Barthélemy = '590',_('590')
    Belarus = "375", _("375")
    Belize = "501", _("501")
    Bermuda = "1441", _("1441")
    Bolivia = "591", _("591")
    Brazil = "55", _("55")
    Barbados = "1246", _("1246")
    Brunei = "673", _("673")
    Bhutan = "975", _("975")
    Botswana = "267", _("267")
    Central_African_Republic = "236", _("236")
    # Canada = '1',_('1')
    # Cocos_eeling_Islands = '61',_('61')
    Switzerland = "41", _("41")
    Chile = "56", _("56")
    China = "86", _("86")
    Ivory_Coast = "225", _("225")
    Cameroon = "237", _("237")
    DR = "243", _("243")
    Republic_of_the_Congo = "242", _("242")
    Cook_Islands = "682", _("682")
    Colombia = "57", _("57")
    Comoros = "269", _("269")
    Cape_Verde = "238", _("238")
    Costa_Rica = "506", _("506")
    Cuba = "53", _("53")
    Curaçao = "5999", _("5999")
    # Christmas_Island = '61',_('61')
    Cayman_Islands = "1345", _("1345")
    Cyprus = "357", _("357")
    Czech_Republic = "420", _("420")
    Germany = "49", _("49")
    Djibouti = "253", _("253")
    Dominica = "1767", _("1767")
    Denmark = "45", _("45")
    Dominican_Republic = "1809", _("1809")
    Dominican_Republic2 = "1829", _("1829")
    Dominican_Republic3 = "1849", _("1849")
    Algeria = "213", _("213")
    Ecuador = "593", _("593")
    Egypt = "20", _("20")
    Eritrea = "291", _("291")
    # Western_Sahara = '212',_('212')
    Spain = "34", _("34")
    Estonia = "372", _("372")
    Ethiopia = "251", _("251")
    # Finland = '358',_('358')
    Fiji = "679", _("679")
    # Falkland_Islands = '500',_('500')
    France = "33", _("33")
    Faroe_Islands = "298", _("298")
    Micronesia = "691", _("691")
    Gabon = "241", _("241")
    United_Kingdom = "44", _("44")
    Georgia = "995", _("995")
    # Guernsey = '44',_('44')
    Ghana = "233", _("233")
    Gibraltar = "350", _("350")
    Guinea = "224", _("224")
    # Guadeloupe = '590',_('590')
    Gambia = "220", _("220")
    Guinea_Bissau = "245", _("245")
    Equatorial_Guinea = "240", _("240")
    Greece = "30", _("30")
    Grenada = "1473", _("1473")
    Greenland = "299", _("299")
    Guatemala = "502", _("502")
    French_Guiana = "594", _("594")
    Guam = "1671", _("1671")
    Guyana = "592", _("592")
    Hong_Kong = "852", _("852")
    Honduras = "504", _("504")
    Croatia = "385", _("385")
    Haiti = "509", _("509")
    Hungary = "36", _("36")
    Indonesia = "62", _("62")
    # Isle_of_Man = '44',_('44')
    India = "91", _("91")
    British_Indian_Ocean_Territory = "246", _("246")
    Ireland = "353", _("353")
    Iran = "98", _("98")
    Iraq = "964", _("964")
    Iceland = "354", _("354")
    Israel = "972", _("972")
    Italy = "39", _("39")
    Jamaica = "1876", _("1876")
    # Jersey = '44',_('44')
    Jordan = "962", _("962")
    Japan = "81", _("81")
    Kazakhstan = "76", _("76")
    Kazakhstan2 = "77", _("77")
    Kenya = "254", _("254")
    Kyrgyzstan = "996", _("996")
    Cambodia = "855", _("855")
    Kiribati = "686", _("686")
    Saint_Kitts_and_Nevis = "1869", _("1869")
    South_Korea = "82", _("82")
    Kosovo = "383", _("383")
    Kuwait = "965", _("965")
    Laos = "856", _("856")
    Lebanon = "961", _("961")
    Liberia = "231", _("231")
    Libya = "218", _("218")
    Saint_Lucia = "1758", _("1758")
    Liechtenstein = "423", _("423")
    Sri_Lanka = "94", _("94")
    Lesotho = "266", _("266")
    Lithuania = "370", _("370")
    Luxembourg = "352", _("352")
    Latvia = "371", _("371")
    Macau = "853", _("853")
    Saint_Martin = "590", _("590")
    Morocco = "212", _("212")
    Monaco = "377", _("377")
    Moldova = "373", _("373")
    Madagascar = "261", _("261")
    Maldives = "960", _("960")
    Mexico = "52", _("52")
    Marshall_Islands = "692", _("692")
    Macedonia = "389", _("389")
    Mali = "223", _("223")
    Malta = "356", _("356")
    Myanmar = "95", _("95")
    Montenegro = "382", _("382")
    Mongolia = "976", _("976")
    Northern_Mariana_Islands = "1670", _("1670")
    Mozambique = "258", _("258")
    Mauritania = "222", _("222")
    Montserrat = "1664", _("1664")
    Martinique = "596", _("596")
    Mauritius = "230", _("230")
    Malawi = "265", _("265")
    Malaysia = "60", _("60")
    Mayotte = "262", _("262")
    Namibia = "264", _("264")
    New_Caledonia = "687", _("687")
    Niger = "227", _("227")
    Norfolk_Island = "672", _("672")
    Nigeria = "234", _("234")
    Nicaragua = "505", _("505")
    Niue = "683", _("683")
    Netherlands = "31", _("31")
    Norway = "47", _("47")
    Nepal = "977", _("977")
    Nauru = "674", _("674")
    New_Zealand = "64", _("64")
    Oman = "968", _("968")
    Pakistan = "92", _("92")
    Panama = "507", _("507")
    # Pitcairn_Islands = '64',_('64')
    Peru = "51", _("51")
    Philippines = "63", _("63")
    Palau = "680", _("680")
    Papua_New_Guinea = "675", _("675")
    Poland = "48", _("48")
    Puerto_Rico = "1787", _("1787")
    Puerto_Rico2 = "1939", _("1939")
    North_Korea = "850", _("850")
    Portugal = "351", _("351")
    Paraguay = "595", _("595")
    Palestine = "970", _("970")
    French_Polynesia = "689", _("689")
    Qatar = "974", _("974")
    # Réunion = '262',_('262')
    Romania = "40", _("40")
    Russia = "7", _("7")
    Rwanda = "250", _("250")
    Saudi_Arabia = "966", _("966")
    Sudan = "249", _("249")
    Senegal = "221", _("221")
    Singapore = "65", _("65")
    South_Georgia = "500", _("500")
    Svalbard_and_Jan_Mayen = "4779", _("4779")
    Solomon_Islands = "677", _("677")
    Sierra_Leone = "232", _("232")
    El_Salvador = "503", _("503")
    San_Marino = "378", _("378")
    Somalia = "252", _("252")
    Saint_Pierre_and_Miquelon = "508", _("508")
    Serbia = "381", _("381")
    South_Sudan = "211", _("211")
    Sao_Tome_and_Principe = "239", _("239")
    Suriname = "597", _("597")
    Slovakia = "421", _("421")
    Slovenia = "386", _("386")
    Sweden = "46", _("46")
    Swaziland = "268", _("268")
    Sint_Maarten = "1721", _("1721")
    Seychelles = "248", _("248")
    Syria = "963", _("963")
    Turks_and_Caicos_Islands = "1649", _("1649")
    Chad = "235", _("235")
    Togo = "228", _("228")
    Thailand = "66", _("66")
    Tajikistan = "992", _("992")
    Tokelau = "690", _("690")
    Turkmenistan = "993", _("993")
    Timor_Leste = "670", _("670")
    Tonga = "676", _("676")
    Trinidad_and_Tobago = "1868", _("1868")
    Tunisia = "216", _("216")
    Turkey = "90", _("90")
    Tuvalu = "688", _("688")
    Taiwan = "886", _("886")
    Tanzania = "255", _("255")
    Uganda = "256", _("256")
    Ukraine = "380", _("380")
    Uruguay = "598", _("598")
    United_States = "1", _("1")
    Uzbekistan = "998", _("998")
    Vatican_City = "3906698", _("3906698")
    Vatican_City2 = "379", _("379")
    Saint_Vincent_and_the_Grenadines = "1784", _("1784")
    Venezuela = "58", _("58")
    British_Virgin_Islands = "1284", _("1284")
    United_States_Virgin_Islands = "1340", _("1340")
    Vietnam_and_Futuna = "84", _("84")
    Vanuatu = "678", _("678")
    Wallis = "681", _("681")
    Samoa = "685", _("685")
    Yemen = "967", _("967")
    South_Africa = "27", _("27")
    Zambia = "260", _("260")
    Zimbabwe = "263", _("263")
