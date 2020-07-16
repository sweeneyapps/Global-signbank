# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20170331_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='gloss',
            name='excludeFromEcv',
            field=models.NullBooleanField(default=False, verbose_name='Exclude from ECV'),
        ),
        migrations.AlterField(
            model_name='definition',
            name='role',
            field=models.CharField(max_length=20, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='final_loc',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('23', 'Cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('4', 'Shoulder'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('86', 'Shoulder contra > shoulder ipsi'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('50', 'Wrist')], null=True, verbose_name='Final Primary Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='final_secondary_loc',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('23', 'Cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('4', 'Shoulder'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('86', 'Shoulder contra > shoulder ipsi'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('50', 'Wrist')], max_length=20, null=True, verbose_name='Final Subordinate Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='initial_secondary_loc',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('23', 'Cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('4', 'Shoulder'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('86', 'Shoulder contra > shoulder ipsi'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('50', 'Wrist')], max_length=20, null=True, verbose_name='Initial Subordinate Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='locPrimLH',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('23', 'Cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('4', 'Shoulder'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('86', 'Shoulder contra > shoulder ipsi'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('50', 'Wrist')], max_length=5, null=True, verbose_name='Placement Active Articulator LH'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='locprim',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('23', 'Cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('4', 'Shoulder'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('86', 'Shoulder contra > shoulder ipsi'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('50', 'Wrist')], max_length=20, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='locsecond',
            field=models.IntegerField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('21', 'Arm'), ('83', 'Back'), ('37', 'Back of head'), ('26', 'Belly'), ('14', 'Belly + forehead'), ('23', 'Cheek'), ('108', 'Cheek > chin'), ('72', 'Cheek contra'), ('16', 'Cheekbone'), ('8', 'Chest'), ('35', 'Chest > trunk'), ('74', 'Chest contra'), ('12', 'Chin'), ('70', 'Chin > chest'), ('28', 'Chin > neutral space'), ('102', 'Chin > weak hand: index finger'), ('33', 'Chin > weak hand: palm'), ('117', 'Chin > weak hand: thumb side'), ('18', 'Ear'), ('84', 'Ear > cheek'), ('124', 'Ear > chest'), ('77', 'Elbow'), ('15', 'Eye'), ('120', 'Eye > neutral space'), ('17', 'Face'), ('110', 'Face > head'), ('93', 'Flank'), ('7', 'Forehead'), ('34', 'Forehead > chest'), ('31', 'Forehead > chin'), ('106', 'Forehead > neutral space'), ('104', 'Forehead > weak hand: palm'), ('64', 'Forehead contra'), ('10', 'Head'), ('119', 'Head + neutral space'), ('113', 'Head > chest'), ('69', 'Head > neutral space'), ('32', 'Head > shoulder'), ('107', 'Head > weak hand: palm'), ('30', 'Head ipsi'), ('94', 'Hip'), ('92', 'Horizontal plane'), ('85', 'Knee'), ('45', 'Leg'), ('95', 'Lower arm'), ('19', 'Mouth'), ('114', 'Mouth > cheek'), ('48', 'Mouth > chest'), ('13', 'Mouth > chin'), ('58', 'Mouth > weak hand'), ('112', 'Mouth > weak hand: palm'), ('9', 'Neck'), ('52', 'Neck > chest'), ('75', 'Neck contra'), ('3', 'Neutral space'), ('2', 'Neutral space > head'), ('121', 'Neutral space > nose'), ('29', 'Neutral space/weak hand: front'), ('22', 'Nose'), ('103', 'Nose > chin'), ('122', 'Nose > neutral space'), ('116', 'Parallel plane'), ('4', 'Shoulder'), ('115', 'Shoulder > shoulder'), ('123', 'Shoulder > weak hand: palm'), ('55', 'Shoulder contra'), ('86', 'Shoulder contra > shoulder ipsi'), ('43', 'Temple'), ('78', 'Temple > chest'), ('79', 'Thumb'), ('27', 'Tongue'), ('97', 'Trunk'), ('54', 'Upper arm'), ('63', 'Upper lip'), ('118', 'Variable'), ('91', 'Virtual object'), ('5', 'Weak hand'), ('6', 'Weak hand > arm'), ('11', 'Weak hand: back'), ('109', 'Weak hand: base'), ('66', 'Weak hand: finger tips'), ('90', 'Weak hand: front'), ('96', 'Weak hand: index finger'), ('98', 'Weak hand: middle finger'), ('36', 'Weak hand: palm'), ('88', 'Weak hand: pinkie'), ('101', 'Weak hand: pinkie side'), ('99', 'Weak hand: ring finger'), ('59', 'Weak hand: thumb'), ('100', 'Weak hand: thumb side'), ('111', 'Weak hand: thumb side > arm'), ('89', 'Weak hand: web space'), ('50', 'Wrist')], null=True, verbose_name='Secondary Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='movDir',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('5', 'Backwards'), ('87', 'Backwards + downwards'), ('93', 'Backwards + ipsilateral'), ('72', 'Backwards + upwards'), ('6', 'Backwards > downwards'), ('15', 'Backwards/forwards'), ('50', 'Contralateral'), ('53', 'Contralateral + downwards'), ('54', 'Contralateral + forwards'), ('52', 'Contralateral + upwards'), ('3', 'Contralateral > forwards'), ('98', 'Distal'), ('8', 'Downwards'), ('56', 'Downwards + forwards'), ('57', 'Downwards + ipsilateral'), ('58', 'Downwards + ipsilateral > downwards'), ('94', 'Downwards + towards'), ('59', 'Downwards > contralateral'), ('4', 'Downwards > forwards'), ('55', 'Downwards > ipsilateral'), ('69', 'Downwards/upwards'), ('90', 'Downwards/upwards + ipsilateral'), ('16', 'Forwards'), ('60', 'Forwards + ipsilateral'), ('61', 'Forwards + upwards'), ('63', 'Forwards > contralateral'), ('17', 'Forwards > downwards'), ('62', 'Forwards > ipsilateral'), ('64', 'Forwards > ipsilateral > forwards'), ('92', 'Forwards > upwards'), ('100', 'From location'), ('101', 'From location > variable'), ('51', 'Ipsilateral'), ('91', 'Ipsilateral + up and down'), ('65', 'Ipsilateral + upwards'), ('71', 'Ipsilateral > contralateral'), ('68', 'Ipsilateral > downwards'), ('66', 'Ipsilateral > downwards > contralateral'), ('67', 'Ipsilateral > upwards'), ('89', 'Ipsilateral and contralateral'), ('88', 'Ipsilateral/contralateral'), ('99', 'Lateral'), ('95', 'Proximal'), ('46', 'To and fro'), ('96', 'Towards location'), ('70', 'Up and down'), ('32', 'Upwards'), ('33', 'Upwards > downwards'), ('73', 'Upwards > forwards > downwards'), ('49', 'Variable')], max_length=5, null=True, verbose_name='Movement Direction'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='relOriLoc',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('8', 'Back'), ('27', 'Back/palm'), ('28', 'Back/palm > palm'), ('3', 'Base'), ('29', 'Counting'), ('4', 'Finger tips'), ('24', 'Finger tips/base'), ('26', 'Fingerspelling'), ('25', 'Front'), ('7', 'Palm'), ('5', 'Radial'), ('2', 'Radial/ulnar'), ('6', 'Ulnar')], max_length=5, null=True, verbose_name='Relative Orientation: Location'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='wordClass',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('5', 'Adjective'), ('7', 'Interjection'), ('2', 'Noun'), ('6', 'Noun or verb'), ('4', 'Particle'), ('3', 'Verb')], max_length=5, null=True, verbose_name='Word class'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='wordClass2',
            field=models.CharField(blank=True, choices=[('0', '-'), ('1', 'N/A'), ('5', 'Adjective'), ('7', 'Interjection'), ('2', 'Noun'), ('6', 'Noun or verb'), ('4', 'Particle'), ('3', 'Verb')], max_length=5, null=True, verbose_name='Word class 2'),
        ),
    ]
