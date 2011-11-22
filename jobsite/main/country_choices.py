from django.utils.translation import ugettext_lazy as _

# Nicely titled (and translatable) country names.
COUNTRIES = (
    ('AF', _(u'Afghanistan')),
    ('AX', _(u'\xc5land Islands')),
    ('AL', _(u'Albania')),
    ('DZ', _(u'Algeria')),
    ('AS', _(u'American Samoa')),
    ('AD', _(u'Andorra')),
    ('AO', _(u'Angola')),
    ('AI', _(u'Anguilla')),
    ('AQ', _(u'Antarctica')),
    ('AG', _(u'Antigua and Barbuda')),
    ('AR', _(u'Argentina')),
    ('AM', _(u'Armenia')),
    ('AW', _(u'Aruba')),
    ('AU', _(u'Australia')),
    ('AT', _(u'Austria')),
    ('AZ', _(u'Azerbaijan')),
    ('BS', _(u'Bahamas')),
    ('BH', _(u'Bahrain')),
    ('BD', _(u'Bangladesh')),
    ('BB', _(u'Barbados')),
    ('BY', _(u'Belarus')),
    ('BE', _(u'Belgium')),
    ('BZ', _(u'Belize')),
    ('BJ', _(u'Benin')),
    ('BM', _(u'Bermuda')),
    ('BT', _(u'Bhutan')),
    ('BO', _(u'Bolivia, Plurinational State of')),
    ('BQ', _(u'Bonaire, Sint Eustatius and Saba')),
    ('BA', _(u'Bosnia and Herzegovina')),
    ('BW', _(u'Botswana')),
    ('BV', _(u'Bouvet Island')),
    ('BR', _(u'Brazil')),
    ('IO', _(u'British Indian Ocean Territory')),
    ('BN', _(u'Brunei Darussalam')),
    ('BG', _(u'Bulgaria')),
    ('BF', _(u'Burkina Faso')),
    ('BI', _(u'Burundi')),
    ('KH', _(u'Cambodia')),
    ('CM', _(u'Cameroon')),
    ('CA', _(u'Canada')),
    ('CV', _(u'Cape Verde')),
    ('KY', _(u'Cayman Islands')),
    ('CF', _(u'Central African Republic')),
    ('TD', _(u'Chad')),
    ('CL', _(u'Chile')),
    ('CN', _(u'China')),
    ('CX', _(u'Christmas Island')),
    ('CC', _(u'Cocos (Keeling) Islands')),
    ('CO', _(u'Colombia')),
    ('KM', _(u'Comoros')),
    ('CG', _(u'Congo')),
    ('CD', _(u'Congo, The Democratic Republic of the')),
    ('CK', _(u'Cook Islands')),
    ('CR', _(u'Costa Rica')),
    ('CI', _(u"C\xf4te D'ivoire")),
    ('HR', _(u'Croatia')),
    ('CU', _(u'Cuba')),
    ('CW', _(u'Cura\xe7ao')),
    ('CY', _(u'Cyprus')),
    ('CZ', _(u'Czech Republic')),
    ('DK', _(u'Denmark')),
    ('DJ', _(u'Djibouti')),
    ('DM', _(u'Dominica')),
    ('DO', _(u'Dominican Republic')),
    ('EC', _(u'Ecuador')),
    ('EG', _(u'Egypt')),
    ('SV', _(u'El Salvador')),
    ('GQ', _(u'Equatorial Guinea')),
    ('ER', _(u'Eritrea')),
    ('EE', _(u'Estonia')),
    ('ET', _(u'Ethiopia')),
    ('FK', _(u'Falkland Islands (Malvinas)')),
    ('FO', _(u'Faroe Islands')),
    ('FJ', _(u'Fiji')),
    ('FI', _(u'Finland')),
    ('FR', _(u'France')),
    ('GF', _(u'French Guiana')),
    ('PF', _(u'French Polynesia')),
    ('TF', _(u'French Southern Territories')),
    ('GA', _(u'Gabon')),
    ('GM', _(u'Gambia')),
    ('GE', _(u'Georgia')),
    ('DE', _(u'Germany')),
    ('GH', _(u'Ghana')),
    ('GI', _(u'Gibraltar')),
    ('GR', _(u'Greece')),
    ('GL', _(u'Greenland')),
    ('GD', _(u'Grenada')),
    ('GP', _(u'Guadeloupe')),
    ('GU', _(u'Guam')),
    ('GT', _(u'Guatemala')),
    ('GG', _(u'Guernsey')),
    ('GN', _(u'Guinea')),
    ('GW', _(u'Guinea-bissau')),
    ('GY', _(u'Guyana')),
    ('HT', _(u'Haiti')),
    ('HM', _(u'Heard Island and McDonald Islands')),
    ('VA', _(u'Holy See (Vatican City State)')),
    ('HN', _(u'Honduras')),
    ('HK', _(u'Hong Kong')),
    ('HU', _(u'Hungary')),
    ('IS', _(u'Iceland')),
    ('IN', _(u'India')),
    ('ID', _(u'Indonesia')),
    ('IR', _(u'Iran, Islamic Republic of')),
    ('IQ', _(u'Iraq')),
    ('IE', _(u'Ireland')),
    ('IM', _(u'Isle of Man')),
    ('IL', _(u'Israel')),
    ('IT', _(u'Italy')),
    ('JM', _(u'Jamaica')),
    ('JP', _(u'Japan')),
    ('JE', _(u'Jersey')),
    ('JO', _(u'Jordan')),
    ('KZ', _(u'Kazakhstan')),
    ('KE', _(u'Kenya')),
    ('KI', _(u'Kiribati')),
    ('KP', _(u"Korea, Democratic People's Republic of")),
    ('KR', _(u'Korea, Republic of')),
    ('KW', _(u'Kuwait')),
    ('KG', _(u'Kyrgyzstan')),
    ('LA', _(u"Lao People's Democratic Republic")),
    ('LV', _(u'Latvia')),
    ('LB', _(u'Lebanon')),
    ('LS', _(u'Lesotho')),
    ('LR', _(u'Liberia')),
    ('LY', _(u'Libyan Arab Jamahiriya')),
    ('LI', _(u'Liechtenstein')),
    ('LT', _(u'Lithuania')),
    ('LU', _(u'Luxembourg')),
    ('MO', _(u'Macao')),
    ('MK', _(u'Macedonia, The Former Yugoslav Republic of')),
    ('MG', _(u'Madagascar')),
    ('MW', _(u'Malawi')),
    ('MY', _(u'Malaysia')),
    ('MV', _(u'Maldives')),
    ('ML', _(u'Mali')),
    ('MT', _(u'Malta')),
    ('MH', _(u'Marshall Islands')),
    ('MQ', _(u'Martinique')),
    ('MR', _(u'Mauritania')),
    ('MU', _(u'Mauritius')),
    ('YT', _(u'Mayotte')),
    ('MX', _(u'Mexico')),
    ('FM', _(u'Micronesia, Federated States of')),
    ('MD', _(u'Moldova, Republic of')),
    ('MC', _(u'Monaco')),
    ('MN', _(u'Mongolia')),
    ('ME', _(u'Montenegro')),
    ('MS', _(u'Montserrat')),
    ('MA', _(u'Morocco')),
    ('MZ', _(u'Mozambique')),
    ('MM', _(u'Myanmar')),
    ('NA', _(u'Namibia')),
    ('NR', _(u'Nauru')),
    ('NP', _(u'Nepal')),
    ('NL', _(u'Netherlands')),
    ('NC', _(u'New Caledonia')),
    ('NZ', _(u'New Zealand')),
    ('NI', _(u'Nicaragua')),
    ('NE', _(u'Niger')),
    ('NG', _(u'Nigeria')),
    ('NU', _(u'Niue')),
    ('NF', _(u'Norfolk Island')),
    ('MP', _(u'Northern Mariana Islands')),
    ('NO', _(u'Norway')),
    ('OM', _(u'Oman')),
    ('PK', _(u'Pakistan')),
    ('PW', _(u'Palau')),
    ('PS', _(u'Palestinian Territory, Occupied')),
    ('PA', _(u'Panama')),
    ('PG', _(u'Papua New Guinea')),
    ('PY', _(u'Paraguay')),
    ('PE', _(u'Peru')),
    ('PH', _(u'Philippines')),
    ('PN', _(u'Pitcairn')),
    ('PL', _(u'Poland')),
    ('PT', _(u'Portugal')),
    ('PR', _(u'Puerto Rico')),
    ('QA', _(u'Qatar')),
    ('RE', _(u'R\xe9union')),
    ('RO', _(u'Romania')),
    ('RU', _(u'Russian Federation')),
    ('RW', _(u'Rwanda')),
    ('BL', _(u'Saint Barth\xe9lemy')),
    ('SH', _(u'Saint Helena, Ascension and Tristan Da Cunha')),
    ('KN', _(u'Saint Kitts and Nevis')),
    ('LC', _(u'Saint Lucia')),
    ('MF', _(u'Saint Martin (French Part)')),
    ('PM', _(u'Saint Pierre and Miquelon')),
    ('VC', _(u'Saint Vincent and the Grenadines')),
    ('WS', _(u'Samoa')),
    ('SM', _(u'San Marino')),
    ('ST', _(u'Sao Tome and Principe')),
    ('SA', _(u'Saudi Arabia')),
    ('SN', _(u'Senegal')),
    ('RS', _(u'Serbia')),
    ('SC', _(u'Seychelles')),
    ('SL', _(u'Sierra Leone')),
    ('SG', _(u'Singapore')),
    ('SX', _(u'Sint Maarten (Dutch Part)')),
    ('SK', _(u'Slovakia')),
    ('SI', _(u'Slovenia')),
    ('SB', _(u'Solomon Islands')),
    ('SO', _(u'Somalia')),
    ('ZA', _(u'South Africa')),
    ('GS', _(u'South Georgia and the South Sandwich Islands')),
    ('SS', _(u'South Sudan')),
    ('ES', _(u'Spain')),
    ('LK', _(u'Sri Lanka')),
    ('SD', _(u'Sudan')),
    ('SR', _(u'Suriname')),
    ('SJ', _(u'Svalbard and Jan Mayen')),
    ('SZ', _(u'Swaziland')),
    ('SE', _(u'Sweden')),
    ('CH', _(u'Switzerland')),
    ('SY', _(u'Syrian Arab Republic')),
    ('TW', _(u'Taiwan, Province of China')),
    ('TJ', _(u'Tajikistan')),
    ('TZ', _(u'Tanzania, United Republic of')),
    ('TH', _(u'Thailand')),
    ('TL', _(u'Timor-leste')),
    ('TG', _(u'Togo')),
    ('TK', _(u'Tokelau')),
    ('TO', _(u'Tonga')),
    ('TT', _(u'Trinidad and Tobago')),
    ('TN', _(u'Tunisia')),
    ('TR', _(u'Turkey')),
    ('TM', _(u'Turkmenistan')),
    ('TC', _(u'Turks and Caicos Islands')),
    ('TV', _(u'Tuvalu')),
    ('UG', _(u'Uganda')),
    ('UA', _(u'Ukraine')),
    ('AE', _(u'United Arab Emirates')),
    ('GB', _(u'United Kingdom')),
    ('US', _(u'United States')),
    ('UM', _(u'United States Minor Outlying Islands')),
    ('UY', _(u'Uruguay')),
    ('UZ', _(u'Uzbekistan')),
    ('VU', _(u'Vanuatu')),
    ('VE', _(u'Venezuela, Bolivarian Republic of')),
    ('VN', _(u'Viet Nam')),
    ('VG', _(u'Virgin Islands, British')),
    ('VI', _(u'Virgin Islands, U.S.')),
    ('WF', _(u'Wallis and Futuna')),
    ('EH', _(u'Western Sahara')),
    ('YE', _(u'Yemen')),
    ('ZM', _(u'Zambia')),
    ('ZW', _(u'Zimbabwe')),
)

# Nicely titled country names with duplicates for those which contain a comma
# (containing the non-comma'd version).
COUNTRIES_PLUS = (
    ('AF', _(u'Afghanistan')),
    ('AX', _(u'\xc5land Islands')),
    ('AL', _(u'Albania')),
    ('DZ', _(u'Algeria')),
    ('AS', _(u'American Samoa')),
    ('AD', _(u'Andorra')),
    ('AO', _(u'Angola')),
    ('AI', _(u'Anguilla')),
    ('AQ', _(u'Antarctica')),
    ('AG', _(u'Antigua and Barbuda')),
    ('AR', _(u'Argentina')),
    ('AM', _(u'Armenia')),
    ('AW', _(u'Aruba')),
    ('SH', _(u'Ascension and Tristan Da Cunha Saint Helena')),
    ('AU', _(u'Australia')),
    ('AT', _(u'Austria')),
    ('AZ', _(u'Azerbaijan')),
    ('BS', _(u'Bahamas')),
    ('BH', _(u'Bahrain')),
    ('BD', _(u'Bangladesh')),
    ('BB', _(u'Barbados')),
    ('BY', _(u'Belarus')),
    ('BE', _(u'Belgium')),
    ('BZ', _(u'Belize')),
    ('BJ', _(u'Benin')),
    ('BM', _(u'Bermuda')),
    ('BT', _(u'Bhutan')),
    ('VE', _(u'Bolivarian Republic of Venezuela')),
    ('BO', _(u'Bolivia, Plurinational State of')),
    ('BQ', _(u'Bonaire, Sint Eustatius and Saba')),
    ('BA', _(u'Bosnia and Herzegovina')),
    ('BW', _(u'Botswana')),
    ('BV', _(u'Bouvet Island')),
    ('BR', _(u'Brazil')),
    ('IO', _(u'British Indian Ocean Territory')),
    ('VG', _(u'British Virgin Islands')),
    ('BN', _(u'Brunei Darussalam')),
    ('BG', _(u'Bulgaria')),
    ('BF', _(u'Burkina Faso')),
    ('BI', _(u'Burundi')),
    ('KH', _(u'Cambodia')),
    ('CM', _(u'Cameroon')),
    ('CA', _(u'Canada')),
    ('CV', _(u'Cape Verde')),
    ('KY', _(u'Cayman Islands')),
    ('CF', _(u'Central African Republic')),
    ('TD', _(u'Chad')),
    ('CL', _(u'Chile')),
    ('CN', _(u'China')),
    ('CX', _(u'Christmas Island')),
    ('CC', _(u'Cocos (Keeling) Islands')),
    ('CO', _(u'Colombia')),
    ('KM', _(u'Comoros')),
    ('CG', _(u'Congo')),
    ('CD', _(u'Congo, The Democratic Republic of the')),
    ('CK', _(u'Cook Islands')),
    ('CR', _(u'Costa Rica')),
    ('CI', _(u"C\xf4te D'ivoire")),
    ('HR', _(u'Croatia')),
    ('CU', _(u'Cuba')),
    ('CW', _(u'Cura\xe7ao')),
    ('CY', _(u'Cyprus')),
    ('CZ', _(u'Czech Republic')),
    ('KP', _(u"Democratic People's Republic of Korea")),
    ('DK', _(u'Denmark')),
    ('DJ', _(u'Djibouti')),
    ('DM', _(u'Dominica')),
    ('DO', _(u'Dominican Republic')),
    ('EC', _(u'Ecuador')),
    ('EG', _(u'Egypt')),
    ('SV', _(u'El Salvador')),
    ('GQ', _(u'Equatorial Guinea')),
    ('ER', _(u'Eritrea')),
    ('EE', _(u'Estonia')),
    ('ET', _(u'Ethiopia')),
    ('FK', _(u'Falkland Islands (Malvinas)')),
    ('FO', _(u'Faroe Islands')),
    ('FM', _(u'Federated States of Micronesia')),
    ('FJ', _(u'Fiji')),
    ('FI', _(u'Finland')),
    ('FR', _(u'France')),
    ('GF', _(u'French Guiana')),
    ('PF', _(u'French Polynesia')),
    ('TF', _(u'French Southern Territories')),
    ('GA', _(u'Gabon')),
    ('GM', _(u'Gambia')),
    ('GE', _(u'Georgia')),
    ('DE', _(u'Germany')),
    ('GH', _(u'Ghana')),
    ('GI', _(u'Gibraltar')),
    ('GR', _(u'Greece')),
    ('GL', _(u'Greenland')),
    ('GD', _(u'Grenada')),
    ('GP', _(u'Guadeloupe')),
    ('GU', _(u'Guam')),
    ('GT', _(u'Guatemala')),
    ('GG', _(u'Guernsey')),
    ('GN', _(u'Guinea')),
    ('GW', _(u'Guinea-bissau')),
    ('GY', _(u'Guyana')),
    ('HT', _(u'Haiti')),
    ('HM', _(u'Heard Island and McDonald Islands')),
    ('VA', _(u'Holy See (Vatican City State)')),
    ('HN', _(u'Honduras')),
    ('HK', _(u'Hong Kong')),
    ('HU', _(u'Hungary')),
    ('IS', _(u'Iceland')),
    ('IN', _(u'India')),
    ('ID', _(u'Indonesia')),
    ('IR', _(u'Iran, Islamic Republic of')),
    ('IQ', _(u'Iraq')),
    ('IE', _(u'Ireland')),
    ('IR', _(u'Islamic Republic of Iran')),
    ('IM', _(u'Isle of Man')),
    ('IL', _(u'Israel')),
    ('IT', _(u'Italy')),
    ('JM', _(u'Jamaica')),
    ('JP', _(u'Japan')),
    ('JE', _(u'Jersey')),
    ('JO', _(u'Jordan')),
    ('KZ', _(u'Kazakhstan')),
    ('KE', _(u'Kenya')),
    ('KI', _(u'Kiribati')),
    ('KP', _(u"Korea, Democratic People's Republic of")),
    ('KR', _(u'Korea, Republic of')),
    ('KW', _(u'Kuwait')),
    ('KG', _(u'Kyrgyzstan')),
    ('LA', _(u"Lao People's Democratic Republic")),
    ('LV', _(u'Latvia')),
    ('LB', _(u'Lebanon')),
    ('LS', _(u'Lesotho')),
    ('LR', _(u'Liberia')),
    ('LY', _(u'Libyan Arab Jamahiriya')),
    ('LI', _(u'Liechtenstein')),
    ('LT', _(u'Lithuania')),
    ('LU', _(u'Luxembourg')),
    ('MO', _(u'Macao')),
    ('MK', _(u'Macedonia, The Former Yugoslav Republic of')),
    ('MG', _(u'Madagascar')),
    ('MW', _(u'Malawi')),
    ('MY', _(u'Malaysia')),
    ('MV', _(u'Maldives')),
    ('ML', _(u'Mali')),
    ('MT', _(u'Malta')),
    ('MH', _(u'Marshall Islands')),
    ('MQ', _(u'Martinique')),
    ('MR', _(u'Mauritania')),
    ('MU', _(u'Mauritius')),
    ('YT', _(u'Mayotte')),
    ('MX', _(u'Mexico')),
    ('FM', _(u'Micronesia, Federated States of')),
    ('MD', _(u'Moldova, Republic of')),
    ('MC', _(u'Monaco')),
    ('MN', _(u'Mongolia')),
    ('ME', _(u'Montenegro')),
    ('MS', _(u'Montserrat')),
    ('MA', _(u'Morocco')),
    ('MZ', _(u'Mozambique')),
    ('MM', _(u'Myanmar')),
    ('NA', _(u'Namibia')),
    ('NR', _(u'Nauru')),
    ('NP', _(u'Nepal')),
    ('NL', _(u'Netherlands')),
    ('NC', _(u'New Caledonia')),
    ('NZ', _(u'New Zealand')),
    ('NI', _(u'Nicaragua')),
    ('NE', _(u'Niger')),
    ('NG', _(u'Nigeria')),
    ('NU', _(u'Niue')),
    ('NF', _(u'Norfolk Island')),
    ('MP', _(u'Northern Mariana Islands')),
    ('NO', _(u'Norway')),
    ('PS', _(u'Occupied Palestinian Territory')),
    ('OM', _(u'Oman')),
    ('PK', _(u'Pakistan')),
    ('PW', _(u'Palau')),
    ('PS', _(u'Palestinian Territory, Occupied')),
    ('PA', _(u'Panama')),
    ('PG', _(u'Papua New Guinea')),
    ('PY', _(u'Paraguay')),
    ('PE', _(u'Peru')),
    ('PH', _(u'Philippines')),
    ('PN', _(u'Pitcairn')),
    ('BO', _(u'Plurinational State of Bolivia')),
    ('PL', _(u'Poland')),
    ('PT', _(u'Portugal')),
    ('TW', _(u'Province of China Taiwan')),
    ('PR', _(u'Puerto Rico')),
    ('QA', _(u'Qatar')),
    ('KR', _(u'Republic of Korea')),
    ('MD', _(u'Republic of Moldova')),
    ('RE', _(u'R\xe9union')),
    ('RO', _(u'Romania')),
    ('RU', _(u'Russian Federation')),
    ('RW', _(u'Rwanda')),
    ('BL', _(u'Saint Barth\xe9lemy')),
    ('SH', _(u'Saint Helena, Ascension and Tristan Da Cunha')),
    ('KN', _(u'Saint Kitts and Nevis')),
    ('LC', _(u'Saint Lucia')),
    ('MF', _(u'Saint Martin (French Part)')),
    ('PM', _(u'Saint Pierre and Miquelon')),
    ('VC', _(u'Saint Vincent and the Grenadines')),
    ('WS', _(u'Samoa')),
    ('SM', _(u'San Marino')),
    ('ST', _(u'Sao Tome and Principe')),
    ('SA', _(u'Saudi Arabia')),
    ('SN', _(u'Senegal')),
    ('RS', _(u'Serbia')),
    ('SC', _(u'Seychelles')),
    ('SL', _(u'Sierra Leone')),
    ('SG', _(u'Singapore')),
    ('BQ', _(u'Sint Eustatius and Saba Bonaire')),
    ('SX', _(u'Sint Maarten (Dutch Part)')),
    ('SK', _(u'Slovakia')),
    ('SI', _(u'Slovenia')),
    ('SB', _(u'Solomon Islands')),
    ('SO', _(u'Somalia')),
    ('ZA', _(u'South Africa')),
    ('GS', _(u'South Georgia and the South Sandwich Islands')),
    ('SS', _(u'South Sudan')),
    ('ES', _(u'Spain')),
    ('LK', _(u'Sri Lanka')),
    ('SD', _(u'Sudan')),
    ('SR', _(u'Suriname')),
    ('SJ', _(u'Svalbard and Jan Mayen')),
    ('SZ', _(u'Swaziland')),
    ('SE', _(u'Sweden')),
    ('CH', _(u'Switzerland')),
    ('SY', _(u'Syrian Arab Republic')),
    ('TW', _(u'Taiwan, Province of China')),
    ('TJ', _(u'Tajikistan')),
    ('TZ', _(u'Tanzania, United Republic of')),
    ('TH', _(u'Thailand')),
    ('CD', _(u'The Democratic Republic of the Congo')),
    ('MK', _(u'The Former Yugoslav Republic of Macedonia')),
    ('TL', _(u'Timor-leste')),
    ('TG', _(u'Togo')),
    ('TK', _(u'Tokelau')),
    ('TO', _(u'Tonga')),
    ('TT', _(u'Trinidad and Tobago')),
    ('TN', _(u'Tunisia')),
    ('TR', _(u'Turkey')),
    ('TM', _(u'Turkmenistan')),
    ('TC', _(u'Turks and Caicos Islands')),
    ('TV', _(u'Tuvalu')),
    ('VI', _(u'U.S. Virgin Islands')),
    ('UG', _(u'Uganda')),
    ('UA', _(u'Ukraine')),
    ('AE', _(u'United Arab Emirates')),
    ('GB', _(u'United Kingdom')),
    ('TZ', _(u'United Republic of Tanzania')),
    ('US', _(u'United States')),
    ('UM', _(u'United States Minor Outlying Islands')),
    ('UY', _(u'Uruguay')),
    ('UZ', _(u'Uzbekistan')),
    ('VU', _(u'Vanuatu')),
    ('VE', _(u'Venezuela, Bolivarian Republic of')),
    ('VN', _(u'Viet Nam')),
    ('VG', _(u'Virgin Islands, British')),
    ('VI', _(u'Virgin Islands, U.S.')),
    ('WF', _(u'Wallis and Futuna')),
    ('EH', _(u'Western Sahara')),
    ('YE', _(u'Yemen')),
    ('ZM', _(u'Zambia')),
    ('ZW', _(u'Zimbabwe')),
)

# Official capitalized country names.
OFFICIAL_COUNTRIES = {
    'AF': u'AFGHANISTAN',
    'AX': u'\xc5LAND ISLANDS',
    'AL': u'ALBANIA',
    'DZ': u'ALGERIA',
    'AS': u'AMERICAN SAMOA',
    'AD': u'ANDORRA',
    'AO': u'ANGOLA',
    'AI': u'ANGUILLA',
    'AQ': u'ANTARCTICA',
    'AG': u'ANTIGUA AND BARBUDA',
    'AR': u'ARGENTINA',
    'AM': u'ARMENIA',
    'AW': u'ARUBA',
    'AU': u'AUSTRALIA',
    'AT': u'AUSTRIA',
    'AZ': u'AZERBAIJAN',
    'BS': u'BAHAMAS',
    'BH': u'BAHRAIN',
    'BD': u'BANGLADESH',
    'BB': u'BARBADOS',
    'BY': u'BELARUS',
    'BE': u'BELGIUM',
    'BZ': u'BELIZE',
    'BJ': u'BENIN',
    'BM': u'BERMUDA',
    'BT': u'BHUTAN',
    'BO': u'BOLIVIA, PLURINATIONAL STATE OF',
    'BQ': u'BONAIRE, SINT EUSTATIUS AND SABA',
    'BA': u'BOSNIA AND HERZEGOVINA',
    'BW': u'BOTSWANA',
    'BV': u'BOUVET ISLAND',
    'BR': u'BRAZIL',
    'IO': u'BRITISH INDIAN OCEAN TERRITORY',
    'BN': u'BRUNEI DARUSSALAM',
    'BG': u'BULGARIA',
    'BF': u'BURKINA FASO',
    'BI': u'BURUNDI',
    'KH': u'CAMBODIA',
    'CM': u'CAMEROON',
    'CA': u'CANADA',
    'CV': u'CAPE VERDE',
    'KY': u'CAYMAN ISLANDS',
    'CF': u'CENTRAL AFRICAN REPUBLIC',
    'TD': u'CHAD',
    'CL': u'CHILE',
    'CN': u'CHINA',
    'CX': u'CHRISTMAS ISLAND',
    'CC': u'COCOS (KEELING) ISLANDS',
    'CO': u'COLOMBIA',
    'KM': u'COMOROS',
    'CG': u'CONGO',
    'CD': u'CONGO, THE DEMOCRATIC REPUBLIC OF THE',
    'CK': u'COOK ISLANDS',
    'CR': u'COSTA RICA',
    'CI': u"C\xd4TE D'IVOIRE",
    'HR': u'CROATIA',
    'CU': u'CUBA',
    'CW': u'CURA\xc7AO',
    'CY': u'CYPRUS',
    'CZ': u'CZECH REPUBLIC',
    'DK': u'DENMARK',
    'DJ': u'DJIBOUTI',
    'DM': u'DOMINICA',
    'DO': u'DOMINICAN REPUBLIC',
    'EC': u'ECUADOR',
    'EG': u'EGYPT',
    'SV': u'EL SALVADOR',
    'GQ': u'EQUATORIAL GUINEA',
    'ER': u'ERITREA',
    'EE': u'ESTONIA',
    'ET': u'ETHIOPIA',
    'FK': u'FALKLAND ISLANDS (MALVINAS)',
    'FO': u'FAROE ISLANDS',
    'FJ': u'FIJI',
    'FI': u'FINLAND',
    'FR': u'FRANCE',
    'GF': u'FRENCH GUIANA',
    'PF': u'FRENCH POLYNESIA',
    'TF': u'FRENCH SOUTHERN TERRITORIES',
    'GA': u'GABON',
    'GM': u'GAMBIA',
    'GE': u'GEORGIA',
    'DE': u'GERMANY',
    'GH': u'GHANA',
    'GI': u'GIBRALTAR',
    'GR': u'GREECE',
    'GL': u'GREENLAND',
    'GD': u'GRENADA',
    'GP': u'GUADELOUPE',
    'GU': u'GUAM',
    'GT': u'GUATEMALA',
    'GG': u'GUERNSEY',
    'GN': u'GUINEA',
    'GW': u'GUINEA-BISSAU',
    'GY': u'GUYANA',
    'HT': u'HAITI',
    'HM': u'HEARD ISLAND AND MCDONALD ISLANDS',
    'VA': u'HOLY SEE (VATICAN CITY STATE)',
    'HN': u'HONDURAS',
    'HK': u'HONG KONG',
    'HU': u'HUNGARY',
    'IS': u'ICELAND',
    'IN': u'INDIA',
    'ID': u'INDONESIA',
    'IR': u'IRAN, ISLAMIC REPUBLIC OF',
    'IQ': u'IRAQ',
    'IE': u'IRELAND',
    'IM': u'ISLE OF MAN',
    'IL': u'ISRAEL',
    'IT': u'ITALY',
    'JM': u'JAMAICA',
    'JP': u'JAPAN',
    'JE': u'JERSEY',
    'JO': u'JORDAN',
    'KZ': u'KAZAKHSTAN',
    'KE': u'KENYA',
    'KI': u'KIRIBATI',
    'KP': u"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
    'KR': u'KOREA, REPUBLIC OF',
    'KW': u'KUWAIT',
    'KG': u'KYRGYZSTAN',
    'LA': u"LAO PEOPLE'S DEMOCRATIC REPUBLIC",
    'LV': u'LATVIA',
    'LB': u'LEBANON',
    'LS': u'LESOTHO',
    'LR': u'LIBERIA',
    'LY': u'LIBYAN ARAB JAMAHIRIYA',
    'LI': u'LIECHTENSTEIN',
    'LT': u'LITHUANIA',
    'LU': u'LUXEMBOURG',
    'MO': u'MACAO',
    'MK': u'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',
    'MG': u'MADAGASCAR',
    'MW': u'MALAWI',
    'MY': u'MALAYSIA',
    'MV': u'MALDIVES',
    'ML': u'MALI',
    'MT': u'MALTA',
    'MH': u'MARSHALL ISLANDS',
    'MQ': u'MARTINIQUE',
    'MR': u'MAURITANIA',
    'MU': u'MAURITIUS',
    'YT': u'MAYOTTE',
    'MX': u'MEXICO',
    'FM': u'MICRONESIA, FEDERATED STATES OF',
    'MD': u'MOLDOVA, REPUBLIC OF',
    'MC': u'MONACO',
    'MN': u'MONGOLIA',
    'ME': u'MONTENEGRO',
    'MS': u'MONTSERRAT',
    'MA': u'MOROCCO',
    'MZ': u'MOZAMBIQUE',
    'MM': u'MYANMAR',
    'NA': u'NAMIBIA',
    'NR': u'NAURU',
    'NP': u'NEPAL',
    'NL': u'NETHERLANDS',
    'NC': u'NEW CALEDONIA',
    'NZ': u'NEW ZEALAND',
    'NI': u'NICARAGUA',
    'NE': u'NIGER',
    'NG': u'NIGERIA',
    'NU': u'NIUE',
    'NF': u'NORFOLK ISLAND',
    'MP': u'NORTHERN MARIANA ISLANDS',
    'NO': u'NORWAY',
    'OM': u'OMAN',
    'PK': u'PAKISTAN',
    'PW': u'PALAU',
    'PS': u'PALESTINIAN TERRITORY, OCCUPIED',
    'PA': u'PANAMA',
    'PG': u'PAPUA NEW GUINEA',
    'PY': u'PARAGUAY',
    'PE': u'PERU',
    'PH': u'PHILIPPINES',
    'PN': u'PITCAIRN',
    'PL': u'POLAND',
    'PT': u'PORTUGAL',
    'PR': u'PUERTO RICO',
    'QA': u'QATAR',
    'RE': u'R\xc9UNION',
    'RO': u'ROMANIA',
    'RU': u'RUSSIAN FEDERATION',
    'RW': u'RWANDA',
    'BL': u'SAINT BARTH\xc9LEMY',
    'SH': u'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA',
    'KN': u'SAINT KITTS AND NEVIS',
    'LC': u'SAINT LUCIA',
    'MF': u'SAINT MARTIN (FRENCH PART)',
    'PM': u'SAINT PIERRE AND MIQUELON',
    'VC': u'SAINT VINCENT AND THE GRENADINES',
    'WS': u'SAMOA',
    'SM': u'SAN MARINO',
    'ST': u'SAO TOME AND PRINCIPE',
    'SA': u'SAUDI ARABIA',
    'SN': u'SENEGAL',
    'RS': u'SERBIA',
    'SC': u'SEYCHELLES',
    'SL': u'SIERRA LEONE',
    'SG': u'SINGAPORE',
    'SX': u'SINT MAARTEN (DUTCH PART)',
    'SK': u'SLOVAKIA',
    'SI': u'SLOVENIA',
    'SB': u'SOLOMON ISLANDS',
    'SO': u'SOMALIA',
    'ZA': u'SOUTH AFRICA',
    'GS': u'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS',
    'SS': u'SOUTH SUDAN',
    'ES': u'SPAIN',
    'LK': u'SRI LANKA',
    'SD': u'SUDAN',
    'SR': u'SURINAME',
    'SJ': u'SVALBARD AND JAN MAYEN',
    'SZ': u'SWAZILAND',
    'SE': u'SWEDEN',
    'CH': u'SWITZERLAND',
    'SY': u'SYRIAN ARAB REPUBLIC',
    'TW': u'TAIWAN, PROVINCE OF CHINA',
    'TJ': u'TAJIKISTAN',
    'TZ': u'TANZANIA, UNITED REPUBLIC OF',
    'TH': u'THAILAND',
    'TL': u'TIMOR-LESTE',
    'TG': u'TOGO',
    'TK': u'TOKELAU',
    'TO': u'TONGA',
    'TT': u'TRINIDAD AND TOBAGO',
    'TN': u'TUNISIA',
    'TR': u'TURKEY',
    'TM': u'TURKMENISTAN',
    'TC': u'TURKS AND CAICOS ISLANDS',
    'TV': u'TUVALU',
    'UG': u'UGANDA',
    'UA': u'UKRAINE',
    'AE': u'UNITED ARAB EMIRATES',
    'GB': u'UNITED KINGDOM',
    'US': u'UNITED STATES',
    'UM': u'UNITED STATES MINOR OUTLYING ISLANDS',
    'UY': u'URUGUAY',
    'UZ': u'UZBEKISTAN',
    'VU': u'VANUATU',
    'VE': u'VENEZUELA, BOLIVARIAN REPUBLIC OF',
    'VN': u'VIET NAM',
    'VG': u'VIRGIN ISLANDS, BRITISH',
    'VI': u'VIRGIN ISLANDS, U.S.',
    'WF': u'WALLIS AND FUTUNA',
    'EH': u'WESTERN SAHARA',
    'YE': u'YEMEN',
    'ZM': u'ZAMBIA',
    'ZW': u'ZIMBABWE',
}
