# ----------------------------------------------------------------------------------------------- #
# External Modules Import


# Internal Scripts Import
from symbolic_distributions_analysis_scripts.Bernoulli_Momentus import Bernoulli_Momentus_Analysis_exe
from symbolic_distributions_analysis_scripts.Bernoulli_CentralMomentus import Bernoulli_CentralMomentus_Analysis_exe
# ----------------------------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------------------------- #
# Request Bernoulli Momentus Analysis

# Create the Analysis Dataframe
Bernoulli_Momentus_Analysis_Dataframe = Bernoulli_Momentus_Analysis_exe()

# Defining the Output PathDir
folder_dir = "descriptive_statistics_dataframe_directory/Bernoulli_Analysis_Dataframe/"
archive_name = "Bernoulli_Momentus_Analysis"
archive_extension = ".csv"

# Write the New CSV Archive
Bernoulli_Momentus_Analysis_Dataframe.to_csv(
    path_or_buf = f"{folder_dir}{archive_name}{archive_extension}",
    header = True)
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# Request Bernoulli CentralMomentus Analysis

# Create the Analysis Dataframe
Bernoulli_CentralMomentus_Analysis_Dataframe = Bernoulli_CentralMomentus_Analysis_exe()

# Defining the Output PathDir
folder_dir = "descriptive_statistics_dataframe_directory/Bernoulli_Analysis_Dataframe/"
archive_name = "Bernoulli_CentralMomentus_Analysis"
archive_extension = ".csv"

# Write the New CSV Archive
Bernoulli_CentralMomentus_Analysis_Dataframe.to_csv(
    path_or_buf = f"{folder_dir}{archive_name}{archive_extension}",
    header = True)
# ----------------------------------------------------------------------------------------------- #



