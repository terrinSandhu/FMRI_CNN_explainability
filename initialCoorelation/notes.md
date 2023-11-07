#most impactful factors:

as determined by decision tree && random forest implementation -- the following 5 factors as inputs are the most impactful when sweeping at 5 parameter steps [5:5:90]

Left Deep White Matter Hyperintensity volume (mm3) FLAIR	
Right Deep White Matter Hyperintensity volume (mm3) FLAIR	
Left Periventricular Hyperintensity volume (mm3) FLAIR	Right periventricular Hyperintensity volume (mm3) 
FLAIR	Right cingulum hippocampus FA non zero mean -JHU	
Left cingulum hippocampus FA non zero mean -JHU


##for independent coor

#forest works well on [5:8]
>Mean Squared Error (MSE): 46.53713659855252
>R-squared (R²) Score: 0.4871435556207868
#decison on [11:17]
>Mean Squared Error (MSE): 63.927922276320075
>R-squared (R²) Score: 0.2954906702144632

#BIN INDEXING:

**axes:**  [4,8,10,17,38,53,68,81,83,87,91] 




blank
BD	
Dx	
Age at Visit

##FLAIR- white matter hyperintensity			
Left Deep White Matter Hyperintensity volume (mm3) FLAIR	
Right Deep White Matter Hyperintensity volume (mm3) FLAIR	
Left Periventricular Hyperintensity volume (mm3) FLAIR	
Right periventricular Hyperintensity volume (mm3) FLAIR

##White matter fractional anisotropy (FA) with John Hopkins Univ. (JHU)Atlas	
Right cingulum hippocampus FA non zero mean -JHU	
Left cingulum hippocampus FA non zero mean -JHU

##Gray matter Cerebral Blood Flow (CBF)																				
NZ mean L hippocampus CBF	
NZ mean R hippocampus CBF	
NZ mean L parahippocampal CBF	
NZ mean R parahippocampal CBF	
Left hippocampal plus parahippocampal	
Right hippocampal plus parahippocampal	
Left medial inferior frontal lobe CBF	
Right medial inferior frontal lobe CBF	
Left superiolateral frontal lobe CBF	
Right superiolateral frontal lobe CBF	
Left lateral parietal lobe CBF	
Right lateral parietal lobe CBF	
left medial parietal lobe CBF	
Right medial parietal lobe CBF	
Left frontal Lobe CBF	
Right frontal Lobe CBF	
Left parietal Lobe CBF	
Right parietal Lobe CBF	
Left hemisphere CBF	Right hemisphere CBF	
Whole Brain Gray Matter CBF nz mean

##Gray matter average thickness														
Left medial inferior frontal lobe cortical thickness	
Right medial inferior frontal lobe cortical thickness	
Left superiolateral frontal lobe cortical thickness	
Right superiolateral frontal lobe cortical thickness	
Left medial parietal lobe cortical thickness	
Right medial parietal lobe cortical thickness	
Left lateral parietal lobe cortical thickness	
Right lateral parietal lobe cortical thickness	
Left frontal lobe average cortical thickness	
Right frontal lobe average cortical thickness	
Left parietal lobe average cortical thickness	
Right parietal lobe average cortical thickness	
total left hemisphere average cortical thickness	
total right hemisphere average cortical thickness	
total whole brain average cortical thickness

##Gray matter surface area														
Left medial inferior frontal lobe surface area	
Right medial inferior frontal lobe surface area	
Left superiolateral frontal lobe surface area	
Right superiolateral frontal lobe surface area	
Left medial parietal lobe surface area	
Right medial parietal lobe surface area	
Left lateral parietal lobe surface area	
Right lateral parietal lobe surface area	
Left frontal lobe surface area	
Right frontal lobe surface area	
Left parietal lobe surface area	
Right parietal lobe surface area	
Total Left hemisphere surface area	
Total right hemisphere surface area	total whole brain surface area

#Gray matter Volume												
Left_Lateral_Ventricle V	
Right_Lateral_Ventricle V	
Left_Inf_Lat_Vent V	
Right_Inf_Lat_Vent V	
parahippocampal_Left_V	
parahippocampal_Right_V	
Left_Hippocampus V	
Right_Hippocampus V	
Left hippocampal and parahippocampal volume	
Right hippocampal and parahippocampal volume	
total left hemisphere gray matter volume	
total right hemisphere gray matter volume	
total whole brain gray matter volume

#Resting state functional connectivity- task negative
DMN resting state Z correlation

#Resting state functional connectivity- task positive network
Task positive network Z correlation

#N-back working memory task			
2v1 right anterior cingulate deactivation	
2v1 right parietal lobule activation	
2v1 left middle frontal gyrus activation	
2v1 right middle frontal gyrus activation

#Delayed match to sample (DMS) working memory task			
Left middle frontal gyrus DMS activation	
Right middle frontal gyrus DMS activation	
Left supramarginal (parietal) gyrus DMS activation	
Right supramarginal (parietal) gyrus DMS activation