from django.db import models
from django.db import models

# ANTI_BODIES = (
#     ('Actin', 'Actin'),
#     ('Smooth_Muscle', 'Smooth_Muscle'),
#     ('Anti_Alpha_Fetoprotein_AFP', 'Anti_Alpha_Fetoprotein_AFP'),
#     ('Anaplastic_Lymphoma_Kinase_ALK_Protin',
#     ('Anaplastic_Lymphoma_Kinase_ALK_Protin'),
#     ('Alpha_Human_Chorionic_Gonadotropin', 'Alpha_Human_Chorionic_Gonadotropin'),
#     ('AMACR', 'AMACR'),
#     ('Androgen_Receptor', 'Androgen_Receptor'),
#     ('ATRX', 'ATRX'),
#     ('Bcl_2_Protein', 'Bcl_2_Protein'),
#     ('Beta_Catenin', 'Beta_Catenin'),
#     ('BRCA_1_Protein', 'BRCA_1_Protein'),
#     ('BCL_6', 'BCL_6'),
#     ('BER_EP4_EPCAM', 'BER_EP4_EPCAM'),
#     ('CDX2', 'CDX2'),
#     ('CA_125', 'CA_125'),
#     ('CD1A', 'CD1A'),
#     ('CD_2', 'CD_2'),
#     ('CD_3', 'CD_3'),
#     ('CD_4', 'CD_4'),
#     ('CD_5', 'CD_5'),
#     ('CD_7', 'CD_7'),
#     ('CD_8', 'CD_8'),
#     ('CD_9', 'CD_9'),
#     ('CD_10', 'CD_10'),
#     ('CD_13', 'CD_13'),
#     ('CD_15', 'CD_15'),
#     ('CD_20', 'CD_20'),
#     ('CD_21', 'CD_21'),
#     ('CD_23', 'CD_23'),
#     ('CD_25', 'CD_25'),
#     ('CD_30', 'CD_30'),
#     ('CD_31', 'CD_31'),
#     ('CD_34', 'CD_34'),
#     ('CD_38', 'CD_38'),
#     ('CD_43', 'CD_43'),
#     ('CD_45RB', 'CD_45RB'),
#     ('CD_45RO', 'CD_45RO'),
#     ('CD_56', 'CD_56'),
#     ('CD_57', 'CD_57'),
#     ('CD_61', 'CD_61'),
#     ('CD_68', 'CD_68'),
#     ('CD_79a', 'CD_79a'),
#     ('CD_99', 'CD_99'),
#     ('CD_105', 'CD_105'),
#     ('CD_117_C_kit', 'CD_117_C_kit'),
#     ('CD_123', 'CD_123'),
#     ('CD_138', 'CD_138'),
#     ('CD_163', 'CD_163'),
#     ('Cytokeratin_5_6', 'Cytokeratin_5_6'),
#     ('Cytokeratin_7', 'Cytokeratin_7'),
#     ('Cytokeratin_10', 'Cytokeratin_10'),
#     ('Cytokeratin_13', 'Cytokeratin_13'),
#     ('Cytokeratin_8_18', 'Cytokeratin_8_18'),
#     ('Cytokeratin_14', 'Cytokeratin_14'),
#     ('Cytokeratin_15', 'Cytokeratin_15'),
#     ('Cytokeratin_17', 'Cytokeratin_17'),
#     ('Cytokeratin_19', 'Cytokeratin_19'),
#     ('Cytokeratin_20', 'Cytokeratin_20'),
#     ('Cytokeratin_High_molecular_weight_34ß12',
#      'Cytokeratin_High_molecular_weight_34ß12'),
#     ('CEA_Carcinoembryonicantigen_Monoclonal',
#      'CEA_Carcinoembryonicantigen_Monoclonal'),
#     ('CEA_Carcinoembryonic_antigen_Polyclonal',
#      'CEA_Carcinoembryonic_antigen_Polyclonal'),
#     ('Chromogranin', 'Chromogranin'),
#     ('Calponin', 'Calponin'),
#     ('Cytokeratin_Low_Molecular_Weight_AE1',
#      'Cytokeratin_Low_Molecular_Weight_AE1'),
#     ('C_Myc_protein', 'C_Myc_protein'),
#     ('Calcitonin', 'Calcitonin'),
#     ('Calretinin', 'Calretinin'),
#     ('Cyclin_D1', 'Cyclin_D1'),
#     ('Caldesmon_HMW', 'Caldesmon_HMW'),
#     ('Desmin', 'Desmin'),
#     ('Dog_1', 'Dog_1'),
#     ('D240', 'D240'),
#     ('E_cadherin', 'E_cadherin'),
#     ('Epidermal_Growth_Factor_Receptor', 'Epidermal_Growth_Factor_Receptor'),
#     ('Epithelial_Membrane_Antigen', 'Epithelial_Membrane_Antigen'),
#     ('Epstein_barr_virus_EBV', 'Epstein_barr_virus_EBV'),
#     ('Estrogen_Receptor', 'Estrogen_Receptor'),
#     ('Factor_VII_Antigen', 'Factor_VII_Antigen'),
#     ('Factor_VIIIa_Antigen', 'Factor_VIIIa_Antigen'),
#     ('GATA_3', 'GATA_3'),
#     ('Glypican_3', 'Glypican_3'),
#     ('Glial_Fibrillary_Acidic_Protein', 'Glial_Fibrillary_Acidic_Protein'),
#     ('GCET_1', 'GCET_1'),
#     ('Gross_Cyctic_Disease_Fluid_Protein_15',
#      'Gross_Cyctic_Disease_Fluid_Protein_15'),
#     ('HBME_1', 'HBME_1'),
#     ('Hepatocyte_Hepar_1', 'Hepatocyte_Hepar_1'),
#     ('Hepatitis_C_Virus', 'Hepatitis_C_Virus'),
#     ('Hepatitis_B_Virus_core_antigen_HBcAg',
#      'Hepatitis_B_Virus_core_antigen_HBcAg'),
#     ('Her_2_neu_C_Erb_B2_Protein', 'Her_2_neu_C_Erb_B2_Protein'),
#     ('HMB_45_Melanoma', 'HMB_45_Melanoma'),
#     ('HPL', 'HPL'),
#     ('HCG', 'HCG'),
#     ('INI_1', 'INI_1'),
#     ('IgG4', 'IgG4'),
#     ('IDH_1', 'IDH_1'),
#     ('Inhibin_Alpha', 'Inhibin_Alpha'),
#     ('Kappa', 'Kappa'),
#     ('Ki_67', 'Ki_67'),
#     ('Lambda', 'Lambda'),
#     ('Langerin', 'Langerin'),
#     ('Lecocyte_Common_Antigen_CD_45', 'Lecocyte_Common_Antigen_CD_45'),
#     ('MDM2', 'MDM2'),
#     ('MUM_1', 'MUM_1'),
#     ('Mammaglobin', 'Mammaglobin'),
#     ('Myogenin', 'Myogenin'),
#     ('Myoglobin', 'Myoglobin'),
#     ('Melan_A_MART_1', 'Melan_A_MART_1'),
#     ('Myeloperoxidase', 'Myeloperoxidase'),
#     ('Muscle_Specific_Actin', 'Muscle_Specific_Actin'),
#     ('Myelin', 'Myelin'),
#     ('MOC_31', 'MOC_31'),
#     ('MMP_13', 'MMP_13'),
#     ('MUC_4', 'MUC_4'),
#     ('MYO_D1', 'MYO_D1'),
#     ('NAPSIN_A', 'NAPSIN_A'),
#     ('Neurofilament', 'Neurofilament'),
#     ('Oct_3_4', 'Oct_3_4'),
#     ('Osteopontin', 'Osteopontin'),
#     ('PD1', 'PD1'),
#     ('PAX_5', 'PAX_5'),
#     ('PAX_8', 'PAX_8'),
#     ('Placental_lactogen_hPL', 'Placental_lactogen_hPL'),
#     ('P63_Protein', 'P63_Protein'),
#     ('Pan_Cytokeratin_AE1_AE3', 'Pan_Cytokeratin_AE1_AE3'),
#     ('Progestrone_Receptor', 'Progestrone_Receptor'),
#     ('Prostate_Specific_Antigen_PSA', 'Prostate_Specific_Antigen_PSA'),
#     ('P53_Protein', 'P53_Protein'),
#     ('PLAP_Placental_alkaline_phosphate', 'PLAP_Placental_alkaline_phosphate'),
#     ('P504S', 'P504S'),
#     ('SOX_11', 'SOX_11'),
#     ('S_100_Protein', 'S_100_Protein'),
#     ('SALL_4', 'SALL_4'),
#     ('Synaptophysin', 'Synaptophysin'),
#     ('TAG_72', 'TAG_72'),
#     ('TFE_3', 'TFE_3'),
#     ('TLE_1', 'TLE_1'),
#     ('Terminal_Deoxynucleotidyl_Transferase_TdT',
#      'Terminal_Deoxynucleotidyl_Transferase_TdT'),
#     ('TdT_Monoclonal', 'TdT_Monoclonal'),
#     ('TTF_1_Thyroid_Transcription_Factor_1',
#      'TTF_1_Thyroid_Transcription_Factor_1'),
#     ('Thyroglobulin', 'Thyroglobulin'),
#     ('Sat_B2', 'Sat_B2'),
#     ('Vimentin', 'Vimentin'),
#     ('VILLIN', 'VILLIN'),
#     ('UROPLAKIN_III', 'UROPLAKIN_III'),
#     ('WT_1_Protein', 'WT_1_Protein'),
#     ('Nestin', 'Nestin'),
#     ('Annexin_A1', 'Annexin_A1'),
#     ('FLE_1', 'FLE_1'),
#     ('SOX_10', 'SOX_10'),
#     ('CDK_4', 'CDK_4')
# )

STATE = (
    ('CASE CREATED', 'CASE CREATED'),
    ('CASE ONGOING', 'CASE ONGOING'),
    ('CASE COMPLETED', 'CASE COMPLETED'),
    ('CASE DIAGNOSED', 'CASE DIAGNOSED')
)

class AntiBodies(models.Model):
    class Meta:
        verbose_name = 'AntiBody'
        verbose_name_plural = 'AntiBodies'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ReferringDoctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Panel(models.Model):
    name = models.CharField(max_length=100)
    anti_bodies = models.ManyToManyField(AntiBodies)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def antibody_names(self):
        return ', '.join([a.name for a in self.anti_bodies.all()])
    anti_bodies.short_description = "AntiBody Names"

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    dob = models.DateTimeField()
    referring_doctor = models.ForeignKey(ReferringDoctor, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=1000, null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    panels = models.ManyToManyField(Panel, null=True, blank=True)

    def panel_names(self):
        return ', '.join([a.name for a in self.panels.all()])
    panels.short_description = "Panel Names"

    def __str__(self):
        return self.name
