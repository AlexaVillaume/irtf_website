# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class EquivWidths(models.Model):
    name = models.TextField(db_column='Name', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nai082 = models.TextField(db_column='naI082', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ca_ii1 = models.TextField(db_column='ca_II1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ca_ii2 = models.TextField(db_column='ca_II2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ca_ii3 = models.TextField(db_column='ca_II3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    feh099 = models.TextField(blank=True, null=True)  # This field type is a guess.
    ki1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    ki2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cai1981 = models.TextField(blank=True, null=True)  # This field type is a guess.
    cai1982 = models.TextField(blank=True, null=True)  # This field type is a guess.
    co2301 = models.TextField(blank=True, null=True)  # This field type is a guess.
    co2302 = models.TextField(blank=True, null=True)  # This field type is a guess.
    ca4227 = models.TextField(db_column='Ca4227', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    g4300 = models.TextField(db_column='G4300', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe4383 = models.TextField(db_column='Fe4383', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ca4455 = models.TextField(db_column='Ca4455', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe4531 = models.TextField(db_column='Fe4531', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    c4668 = models.TextField(db_column='C4668', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hbeta = models.TextField(db_column='Hbeta', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe5015 = models.TextField(db_column='Fe5015', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mgb = models.TextField(db_column='Mgb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe5270 = models.TextField(db_column='Fe5270', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe5335 = models.TextField(db_column='Fe5335', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe5406 = models.TextField(db_column='Fe5406', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe5709 = models.TextField(db_column='Fe5709', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe5782 = models.TextField(db_column='Fe5782', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nad = models.TextField(db_column='NaD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hdeltaa = models.TextField(db_column='HdeltaA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hgammaa = models.TextField(db_column='HgammaA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hdeltaf = models.TextField(db_column='HdeltaF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hgammaf = models.TextField(db_column='HgammaF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mgi8800 = models.TextField(db_column='mgI8800', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nai114 = models.TextField(db_column='naI114', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tio = models.TextField(db_column='TiO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cn1 = models.TextField(db_column='CN1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nai220 = models.TextField(db_column='naI220', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'equiv_widths'


class EwLower(models.Model):
    name = models.TextField(db_column='Name', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ca4227_l = models.TextField(db_column='Ca4227_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    g4300_l = models.TextField(db_column='G4300_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe4383_l = models.TextField(db_column='Fe4383_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca4455_l = models.TextField(db_column='Ca4455_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe4531_l = models.TextField(db_column='Fe4531_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    c4668_l = models.TextField(db_column='C4668_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hbeta_l = models.TextField(db_column='Hbeta_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5015_l = models.TextField(db_column='Fe5015_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    mgb_l = models.TextField(db_column='Mgb_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5270_l = models.TextField(db_column='Fe5270_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5335_l = models.TextField(db_column='Fe5335_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5406_l = models.TextField(db_column='Fe5406_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5709_l = models.TextField(db_column='Fe5709_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5782_l = models.TextField(db_column='Fe5782_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nad_l = models.TextField(db_column='NaD_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hdeltaa_l = models.TextField(db_column='HdeltaA_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hgammaa_l = models.TextField(db_column='HgammaA_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hdeltaf_l = models.TextField(db_column='HdeltaF_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hgammaf_l = models.TextField(db_column='HgammaF_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nai082_l = models.TextField(db_column='naI082_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca_ii1_l = models.TextField(db_column='ca_II1_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca_ii2_l = models.TextField(db_column='ca_II2_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca_ii3_l = models.TextField(db_column='ca_II3_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    feh099_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    ki1_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    ki2_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    cai1981_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    cai1982_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    co2301_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    co2302_l = models.TextField(blank=True, null=False)  # This field type is a guess.
    mgi8800_l = models.TextField(db_column='mgI8800_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nai114_l = models.TextField(db_column='naI114_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    tio_l = models.TextField(db_column='TiO_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    cn1_l = models.TextField(db_column='CN1_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nai220_l = models.TextField(db_column='naI220_l', blank=True, null=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ew_lower'


class EwUpper(models.Model):
    name = models.TextField(db_column='Name', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ca4227_u = models.TextField(db_column='Ca4227_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    g4300_u = models.TextField(db_column='G4300_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe4383_u = models.TextField(db_column='Fe4383_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca4455_u = models.TextField(db_column='Ca4455_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe4531_u = models.TextField(db_column='Fe4531_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    c4668_u = models.TextField(db_column='C4668_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hbeta_u = models.TextField(db_column='Hbeta_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5015_u = models.TextField(db_column='Fe5015_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    mgb_u = models.TextField(db_column='Mgb_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5270_u = models.TextField(db_column='Fe5270_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5335_u = models.TextField(db_column='Fe5335_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5406_u = models.TextField(db_column='Fe5406_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5709_u = models.TextField(db_column='Fe5709_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    fe5782_u = models.TextField(db_column='Fe5782_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nad_u = models.TextField(db_column='NaD_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hdeltaa_u = models.TextField(db_column='HdeltaA_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hgammaa_u = models.TextField(db_column='HgammaA_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hdeltaf_u = models.TextField(db_column='HdeltaF_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    hgammaf_u = models.TextField(db_column='HgammaF_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nai082_u = models.TextField(db_column='naI082_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca_ii1_u = models.TextField(db_column='ca_II1_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca_ii2_u = models.TextField(db_column='ca_II2_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    ca_ii3_u = models.TextField(db_column='ca_II3_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    feh099_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    ki1_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    ki2_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    cai1981_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    cai1982_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    co2301_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    co2302_u = models.TextField(blank=True, null=False)  # This field type is a guess.
    mgi8800_u = models.TextField(db_column='mgI8800_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nai114_u = models.TextField(db_column='naI114_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    tio_u = models.TextField(db_column='TiO_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    cn1_u = models.TextField(db_column='CN1_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.
    nai220_u = models.TextField(db_column='naI220_u', blank=True, null=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ew_upper'


class Mdwarfs(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    teff = models.FloatField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    luminosity = models.FloatField(blank=True, null=True)
    fe_h = models.FloatField(db_column='Fe/H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    spec = models.TextField(blank=True, null=True)
    full_spec = models.TextField(blank=True, null=True)
    distance = models.TextField(blank=True, null=True)
    logg = models.FloatField(blank=True, null=True)
    mod_spec = models.TextField(blank=True, null=True)
    snr_avg = models.FloatField(blank=True, null=True)
    modspecis = models.FloatField(db_column='ModSpecIs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mdwarfs'


class Targets(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    miles = models.TextField(db_column='MILES', blank=True, null=True)  # Field name made lowercase.
    cat = models.TextField(db_column='CaT', blank=True, null=True)  # Field name made lowercase.
    spt = models.TextField(db_column='SpT', blank=True, null=True)  # Field name made lowercase.
    teff = models.IntegerField(db_column='Teff', blank=True, null=True)  # Field name made lowercase.
    logg = models.FloatField(blank=True, null=True)
    fe_h = models.FloatField(db_column='Fe/H', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ref = models.IntegerField(db_column='REF', blank=True, null=True)  # Field name made lowercase.
    libraries = models.TextField(db_column='Libraries', blank=True, null=True)  # Field name made lowercase.
    miles_spec = models.TextField(db_column='MILES_spec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    irtf_spec = models.TextField(db_column='IRTF_spec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    e_b_v_field = models.TextField(db_column='E(B-V)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    miles_spec_2 = models.TextField(db_column='MILES_spec_2', blank=True, null=True)  # Field name made lowercase.
    miles_error = models.TextField(db_column='MILES_error', blank=True, null=True)  # Field name made lowercase.
    v = models.TextField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    v_error = models.TextField(db_column='V_error', blank=True, null=True)  # Field name made lowercase.
    b = models.TextField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    b_error = models.TextField(db_column='B_error', blank=True, null=True)  # Field name made lowercase.
    j = models.TextField(db_column='J', blank=True, null=True)  # Field name made lowercase.
    j_error = models.TextField(db_column='J_error', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    h_error = models.TextField(db_column='H_error', blank=True, null=True)  # Field name made lowercase.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase.
    k_error = models.TextField(db_column='K_error', blank=True, null=True)  # Field name made lowercase.
    w1 = models.TextField(db_column='W1', blank=True, null=True)  # Field name made lowercase.
    w1_error = models.TextField(db_column='W1_error', blank=True, null=True)  # Field name made lowercase.
    w2 = models.TextField(db_column='W2', blank=True, null=True)  # Field name made lowercase.
    w2_error = models.TextField(db_column='W2_error', blank=True, null=True)  # Field name made lowercase.
    w3 = models.TextField(db_column='W3', blank=True, null=True)  # Field name made lowercase.
    w3_error = models.TextField(db_column='W3_error', blank=True, null=True)  # Field name made lowercase.
    w4 = models.TextField(db_column='W4', blank=True, null=True)  # Field name made lowercase.
    w4_error = models.TextField(db_column='W4_error', blank=True, null=True)  # Field name made lowercase.
    number_2mass_q = models.TextField(db_column='2MASS_Q', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    wise_q = models.TextField(db_column='WISE_Q', blank=True, null=True)  # Field name made lowercase.
    mass_q = models.TextField(db_column='MASS_Q', blank=True, null=True)  # Field name made lowercase.
    mass_2 = models.TextField(db_column='MASS_2', blank=True, null=True)  # Field name made lowercase.
    los_v = models.TextField(db_column='LOS_V', blank=True, null=True)  # Field name made lowercase.
    los_sigma = models.TextField(db_column='LOS_sigma', blank=True, null=True)  # Field name made lowercase.
    observed = models.TextField(db_column='Observed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shapeissue = models.TextField(db_column='ShapeIssue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ew = models.TextField(db_column='EW', blank=True, null=True)  # Field name made lowercase.
    zred = models.FloatField(blank=True, null=True)
    teff_p = models.FloatField(db_column='Teff_p', blank=True, null=True)  # Field name made lowercase.
    logg_p = models.FloatField(blank=True, null=True)
    fe_h_p = models.FloatField(db_column='Fe/H_p', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parallax = models.FloatField(blank=True, null=True)
    parallax_error = models.FloatField(blank=True, null=True)
    logl = models.FloatField(blank=True, null=True)
    teff_prug = models.FloatField(blank=True, null=True)
    logg_prug = models.FloatField(blank=True, null=True)
    fe_h_prug = models.FloatField(db_column='Fe/H_prug', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    synmags = models.TextField(db_column='SynMags', blank=True, null=True)  # Field name made lowercase.
    distance = models.FloatField(blank=True, null=True)
    full_spec = models.TextField(blank=True, null=True)
    v_h = models.TextField(db_column='V_H', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    b_h = models.TextField(db_column='B_H', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    parallax_h = models.TextField(db_column='parallax_H', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    snr_med = models.TextField(blank=True, null=True)  # This field type is a guess.
    paramissue = models.TextField(db_column='ParamIssue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qualityissue = models.TextField(db_column='QualityIssue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    teff_sharm = models.FloatField(blank=True, null=True)
    logg_sharm = models.FloatField(blank=True, null=True)
    fe_h_sharm = models.FloatField(db_column='Fe/H_sharm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teff_irfm = models.FloatField(blank=True, null=True)
    ra = models.TextField(db_column='RA', blank=True, null=True)  # Field name made lowercase.
    dec = models.TextField(db_column='DEC', blank=True, null=True)  # Field name made lowercase.
    sdss_i = models.FloatField(blank=True, null=True)
    sdss_i_error = models.FloatField(blank=True, null=True)
    sdss_z = models.FloatField(blank=True, null=True)
    sdss_error = models.FloatField(db_column='sdss__error', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    sdss_z_error = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'targets'
