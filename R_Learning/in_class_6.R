bank_data= 'https://raw.githubusercontent.com/MSUDataAnalytics/SSC442/master/Labs/data/bank.csv'

bank = read.csv(url(bank_data))

full_bank_model = lm(balance ~ ., data = bank)

summary(full_bank_model)

new_bank_model = lm(balance ~ , data = bank)
