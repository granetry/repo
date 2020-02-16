# load raw data
test_data <- 'https://raw.githubusercontent.com/EasyD/IntroToDataScience/master/test.csv'
train_data <- 'https://raw.githubusercontent.com/EasyD/IntroToDataScience/master/train.csv'

train <- read.csv(url(train_data),header = TRUE)
test <- read.csv(url(test_data),header = TRUE)

#
# Add a "Survived" variable to the test set to allow for combining data sets
# data.frame lets you create new data frames
# data.frame(survived =) will add survived to the dataframe
# rep() allows you to replicate, or repeat, values. In this case, repeat "None"
# How long to repeat "None" is dictated by nrow(test), which is the number of rows in test
# test[,] says I want to subset the dataset in all rows and columns, take the entire data frame of test,
# and combine it with a list of strings of "None"
# test[1,4] will locate the value in the first row and fourth column
# 

test.survived <- data.frame(survived = rep("None", nrow(test)), test[,])

#
# Combine data sets
# rbind() stands for row bind. We want to combine the two data frames based on rows
# since we have the same columns
# cbind() would work for columns
#

data.combined <- rbind(train, test.survived)

# 
# A bit about R data types (e.g., factors)
# Running thise cose will list the variables and variable types, the structure.
#

str(data.combined)

#
# This code updates the variable data.combined
# The update happens in pclass, denoted by the "$"
# The pclass is then set to the as.factor() function to turn it into a factor, categorical variable,
# since an integer value does not matter, as it states your socioeconomic status (SES),
# they were either "first", "second", or "third" class
# computers dont like string values, so update survived as a factor.
# remember survived eventually turns to "none" later in data frame due to the earlier data.combined()
#

data.combined$pclass <- as.factor(data.combined$pclass)
data.combined$survived <- as.factor(data.combined$survived)


#
# Take a look at gross survival rates
# This will allow us to see the totals of each input in survived
# 0 = parish, 1 = survived
#

table(data.combined$survived)


#
# Distribution across classes
#

table(data.combined$pclass)

#
# Load up ggplot2 package to use for visualizations
#

library(ggplot2)

#
# Hypothesis - Rich folk survived at a higher rate
# - We can see that the rich did in fact have better survival rates when compared to 3rd class.
#
# Here we needed to make pclass an integer type so we could add them up as a hist().
# Survived needs to be a factor in order for the classification to add the color
#

train$pclass <- as.integer(train$pclass)
train$survived <- as.factor(train$survived)

g = ggplot(train, mapping = aes(x= pclass, fill = survived))

g + theme_bw() + geom_histogram(binwidth = 0.5) + labs(y = "Number of Passangers",
                                                       x = "Ticket Class",
                                                       title = "Survival Rates Across Ticket Class")

