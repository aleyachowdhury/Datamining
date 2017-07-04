#read data
health<-read.csv(file ="HEALTH.csv", head=T, sep=",")
access <- read.csv(file ="ACCESS.csv", head =T, sep=",")
assistance <- read.csv(file="ASSISTANCE.csv", head=T, sep=",")
prices <- read.csv(file="PRICES_TAXES.csv", head=T, sep=",")
restaurants <- read.csv(file="RESTAURANTS.csv", head=T, sep=",")
stores <- read.csv(file="STORES.csv", head=T, sep=",")
socioeconomic <- read.csv(file="SOCIOECONOMIC.csv", head=T, sep=",")
xAttr <- c("PCT_DIABETES_ADULTS10", "PCT_OBESE_ADULTS10", "PCT_OBESE_CHILD11")

attr1 <- character()
attr2 <- character()
correlation <- numeric()


#r = (sumofall(a*b))/(sqrt(sumofall(a^2)*sumofall(b^2)))
# a = x-x_avg, b- y-y_avg

#iter1
#a: PCT_DIABETES_ADULTS10
#iter2
#a: PCT_OBESE_ADULTS13
#iter3
#a: PCT_OBESE_CHILD11
for(n in 1:3){
	#Access
	yAttr <- c("PCT_LACCESS_POP10","PCT_LACCESS_LOWI10", "PCT_LACCESS_CHILD10", "PCT_LACCESS_SENIORS10","PCT_FREE_LUNCH10","PCT_REDUCED_LUNCH10", "PC_WIC_REDEMP12")
	a = health[,xAttr[n]] - mean(health[,xAttr[n]], na.rm=T)

	#iter1
	#b: PCT_LACCESS_POP10
	#iter2
	#b: PCT_LACCESS_LOWI10
	#iter3
	#b: PCT_LACCESS_CHILD10
	#iter4
	#b: PCT_LACCESS_SENIORS10
	for(i in 1:4){
		b = access[,yAttr[i]] - mean(access[,yAttr[i]], na.rm=T)
		r = sum(a*b,na.rm=T)/(sqrt(sum(a*a, na.rm=T)*sum(b*b, na.rm=T)))
		s = sprintf("%s, %s: %f", xAttr[n], yAttr[i], r)
		print(s)
		if(abs(r)>=0.5){
			attr1 <- c(attr1, xAttr[n])
			attr2 <- c(attr2, yAttr[i])
			correlation <- c(correlation, r)
		}
	}

	#Assistance
	yAttr <-c("PCT_FREE_LUNCH10", "PCT_REDUCED_LUNCH10", "PC_WIC_REDEMP08")

	#iter1
	#b: PCT_FREE_LUNCH10
	#iter2
	#b: PCT_REDUCED_LUNCH10
	#iter3
	#b: PC_WIC_REDEMP12
	for(i in 1:3){
		b = assistance[,yAttr[i]] - mean(assistance[,yAttr[i]],na.rm=T)
		r = sum(a*b, na.rm=T)/(sqrt(sum(a*a, na.rm=T)*sum(b*b, na.rm=T)))
		s = sprintf("%s, %s: %f", xAttr[n], yAttr[i], r)
		print(s)
		if(abs(r)>=0.5){
			attr1 <- c(attr1, xAttr[n])
			attr2 <- c(attr2, yAttr[i])
			correlation <- c(correlation, r)
		}
	}


	#Prices
	yAttr <- c("MILK_PRICE10","SODA_PRICE10", "MILK_SODA_PRICE10")

	#iter1
	#b: MILK_PRICE10
	#iter2
	#b: SODA_PRICE10
	#iter3
	#b: MILK_SODA_PRICE10
	for(i in 1:3){
		b = prices[,yAttr[i]] - mean(prices[,yAttr[i]],na.rm=T)
		r = sum(a*b, na.rm=T)/(sqrt(sum(a*a, na.rm=T)*sum(b*b, na.rm=T)))
		s = sprintf("%s, %s: %f", xAttr[n], yAttr[i], r)
		print(s)
		if(abs(r)>=0.5){
			attr1 <- c(attr1, xAttr[n])
			attr2 <- c(attr2, yAttr[i])
			correlation <- c(correlation, r)
		}
	}

	#Restaurants
	yAttr <- c("FFRPTH12", "FSRPTH12")

	#iter1
	#b: FFRPTH12
	#iter2
	#b: FSRPTH12
	for(i in 1:2){
		b = restaurants[,yAttr[i]] - mean(restaurants[,yAttr[i]],na.rm=T)
		r = sum(a*b, na.rm=T)/(sqrt(sum(a*a, na.rm=T)*sum(b*b, na.rm=T)))
		s = sprintf("%s, %s: %f", xAttr[n], yAttr[i], r)
		print(s)
		if(abs(r)>=0.5){
			attr1 <- c(attr1, xAttr[n])
			attr2 <- c(attr2, yAttr[i])
			correlation <- c(correlation, r)
		}
	}
	#Stores
	yAttr<- c("GROCPTH12", "SUPERCPTH12", "CONVSPTH12", "SPECSPTH12")

	#iter1
	#b: GROCPTH12
	#iter2
	#b: SUPERCPTH12
	#iter3
	#b: CONVSPTH12
	#iter4
	#b: SPECSPTH12
	for(i in 1:4){
		b = stores[,yAttr[i]] - mean(stores[,yAttr[i]],na.rm=T)
		r = sum(a*b, na.rm=T)/(sqrt(sum(a*a, na.rm=T)*sum(b*b, na.rm=T)))
		s = sprintf("%s, %s: %f", xAttr[n], yAttr[i], r)
		print(s)
		if(abs(r)>=0.5){
			attr1 <- c(attr1, xAttr[n])
			attr2 <- c(attr2, yAttr[i])
			correlation <- c(correlation, r)
		}
	}
	#Socioeconomic
	yAttr <- c("PCT_NHWHITE10","PCT_NHBLACK10", "PCT_HISP10","PCT_NHASIAN10", "PCT_NHNA10", "PCT_NHPI10", "PCT_65OLDER10", "PCT_18YOUNGER10", "POVRATE10", "CHILDPOVRATE10")
		for(i in 1:10){
		b = socioeconomic[,yAttr[i]] - mean(socioeconomic[,yAttr[i]],na.rm=T)
		r = sum(a*b, na.rm=T)/(sqrt(sum(a*a, na.rm=T)*sum(b*b, na.rm=T)))
		s = sprintf("%s, %s: %f", xAttr[n], yAttr[i], r)
		print(s)
		if(abs(r)>=0.5){
			attr1 <- c(attr1, xAttr[n])
			attr2 <- c(attr2, yAttr[i])
			correlation <- c(correlation, r)
		}
	}
}

strongCorrelations <- data.frame(attr1, attr2, correlation)


print("Strong correlations:")
print(strongCorrelations)


