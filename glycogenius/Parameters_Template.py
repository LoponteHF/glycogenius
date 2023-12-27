[library_building]
use_custom_glycans_list = no
custom_glycans_list = H3N2, H5N2, H5N4S2F1
; Allows you to only search for target glycans by inputing them in the "custom_glycans_list", as formulas. If True, overrides imp_library. Monosaccharides accepted: Hexoses (H), HexNAc (N), Acetyl Sialic Acid (S), Glycolyl Sialic Acid (G), Deoxyhexose (F). Case sensitive.
min_monos = 5
max_monos = 18
min_hex = 3
max_hex = 10
min_hexnac = 2
max_hexnac = 8
min_sia = 0
max_sia = 4
min_fuc = 0
max_fuc = 2
min_ac = 0
max_ac = 4
min_gc = 0
max_gc = 0
; Specify the minimum and maximum monosaccharides amounts for generating a library.
force_nglycan = yes
; Used to force some monosaccharides compositions associated with N-Glycans biologically known features.
max_adducts = H3Na1
; Indicates the desired adducts and their maximum amount. H3Na1 means a maximum of 3 Hydrogens and a maximum of 1 Sodium per adduct combination. Case sensitive.
max_charges = 3
; Limits the maximum amount of calculated charges for each glycan. Set to a negative value if you want to do negative mode analysis.
tag_mass = 133.0644
; If a reducing end tag is added to the glycans, insert its added mass here. If no reducing end tag is added to the glycans, set this value to 0. Procainamide: 219.1735; Girard Reagent P: 133.0644 (deprotonated, neutral)
permethylated = no
; If the sample was permethylated, set this parameter to "yes". Doesn't take into account partial permethylations.
reduced = no
; If the sample doesn't have a tag and the glycans had their reducing end reduced, set this to "yes".
fast_iso = yes
; Allows you to calculate the isotopic distribution of glycans based only on carbon isotopes (fast, innacurate) or on all the atoms isotopes (VERY SLOW, very accurate). If not used, library building may take many hours.
high_resolution_isotopic_dist = no
; If not used, doesn't clump isotope peaks together, meaning that you'll have more than one isotopic peak in a 1 Da interval. Only use this if you have fast_iso on. Useful for when analyzing very high resolution data, such as data acquired on a FT mass spectrometers.
internal_standard_mass = 0.0
; If using an internal standard, insert its mass here for the script to calculate its area.
imp_library = no
; Can be used to import a glycans library previously generated by this script. Glycan library must be in working directory (set below, on analysis_parameters).
exp_library = no
; Export the library you generate to use in future analysis without having to build a new library. Also creates an excel file containing a human-readable version of the library generated.
only_gen_lib = no
; Determines if the script should stop after generating library or proceed with data analysis. 

[analysis_parameters]
multithreaded_analysis = no
threads_number = 20
; Allows you to split the execution and generated library into multiple pieces for multithreaded execution. After running GlycoGenius, there will be several .py files in working directory. Run the ones named Multithreaded_0.py-Multithreaded_n.py in whatever time you want, in how many amounts at a time you want.
analyze_ms2 = yes
force_fragments_to_glycans = yes
unrestricted_fragments = no
; Allows to analyze ms2 data, as well. Fragments identified will be associated with each glycan. You can choose to filter identified fragments by monosaccharides compositions, in order to avoid reporting fragments that aren't compatible with detected precursor. If unrestricted_fragments is used, it searches for glycans in every ms2 scan, regardless if the glycan was found in full scan. This will take a bit longer.
accuracy_unit = mz
; Determines the units of mz tolerance to be used by the script. Options: 'ppm' or 'pw'. 'ppm' = Particles per Million, where 10 ppm is around 0.01 mz tolerance at mz 1000, 'mz' = Fixed mz tolerance from centroid, 0.01 mz means it tolerates a 0.01 variance in mz
accuracy_value = 0.01
; The value for the accuracy_unit parameter. You can use a broader accuracy value and then filter raw data using max_ppm, but this may lead to false positives.
ret_time_begin = 1
ret_time_end = 80
ret_time_tolerance = 0.2
; The minimum and maximum retention time, in minutes, used for various portions of the script. A shorter interval of ret_time makes the script run faster, so try to trim your sample as much as possible, if you know when your analytes are leaving the column. Set the retention time tolerance used for fragments to adduct and same peak identification.
min_isotopologue_peaks = 3
; Minimum amount of isotopologue peaks that an identified glycan mz must have to actually be taken into account by the script. Minimum amount is 2 (second one necessary to confirm charge). May affect isotopic distribution fitting score and can't be recalculated on data reanalysis.
custom_min_points_per_peak = no
number_points_per_peak = 5
; If used, set the minimum number of datapoints to consider a chromatogram peak part of the raw dataset. If left on False it calculates automatically.
limit_peaks_picked = no
max_number_peaks = 5
; If used, picks only the most intense peak on the EIC and up to [max_number_peaks]-1 other peaks closest to it. Warning: This may reduce the range of your results and it can't be changed on reanalysis.
max_ppm = 10
; Maximum PPM for data curation. If value is greater than equivalent accuracy_value, data won't be filtered by this criteria, as it was already filtered during processing by accuracy_value. Can be reapplied on raw data reanalysis.
isotopic_fitting_score = 0.8
; Minimum score of the isotopic distribution fitting in order to consider a mz peak viable. Can be reapplied on raw data reanalysis.
curve_fitting_score = 0.95
; Minimum score for the chromatogram peak curve fitting to a gaussian to consider a viable peak. Can be reapplied on raw data reanalysis.
signal_to_noise = 3
; Minimum signal-to-noise ratio to consider a chromatogram peak viable. Can be reapplied on raw data reanalysis.
custom_noise_level = no
noise_levels = 0, 0
; Sets a custom level of noise for each sample, ignoring the automatic noise calculation. Noise for each sample is comma separated in "noise_levels". Warning: NOT RECOMMENDED unless you're really sure about what you're doing.
samples_path =
; A comma separated list of full path to files to be analyzed together.
working_path =
; Directory to load and save files from script.
plot_metaboanalyst = no
metaboanalyst_groups = CONTROL, TREATED
; Here you set up whether or not you want to output a .csv file to be used for plotting data using metaboanalyst. If you want that, you must specify your sample groups, comma separated. Sample groups specified must be present in sample filenames for proper identification. If none is set, samples are defaulted to "ungrouped". Case sensitive.
reanalysis = no
output_plot_data = no
; Reanalyzes raw data with new max_ppm, isotopic_fitting_score, curve_fitting_score and signal_to_noise criteria. Overrides any other setting besides these mentioned. First parameter  produces a new Results file, second parameter also produces a new Plotting Data file (in case you deleted your original one. The data in it will not be any different than the former one). Warning: If setting a stricter max_ppm criteria on reanalysis without remaking the whole  execution with a new accuracy_value, data may still contain false positives.