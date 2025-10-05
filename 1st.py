import matplotlib.pyplot as plt
import pandas as pd
x=[1,2,3,4]
y=[1,2,3,4]

# plt.plot(x,y)     #Plotting the graph
# plt.grid()      # to have grid in the graph 
# print(plt.show())  #to show the graph

data={
    "Salary":[18000,30000,15000,18000,20000,14000,20000,15000,17000,19000]
}

#to work with dictionaries we have to convert them to dataframes
df=pd.DataFrame(data)

# #                        ********** LINE PLOT ***********
# # plt.plot(df)
# # print(plt.show())

# #can set color ,with of line and can set variables at th values
# plt.plot(df['Salary'],color='red',marker='x',linewidth='5',linestyle='--')
# plt.grid()
# print(plt.show())

#                        ********** HISTOGRAM ***********

# plt.hist(df)

#can set color ,with of line and can set variables at th values
# plt.hist(df,color='red',bins=10)        #bins are no. of plotting in columns
# print(plt.show())

#               ************* BOX PLOT **************

# plt.boxplot(df)
# print(plt.show())

# df.loc[20]=0
# df.drop(index=20,inplace=True)
# plt.boxplot(df)
# print(plt.show())


df["Dept"]=['HR','Sales','Finance','HR','Sales','Finance','HR','Sales','Finance','HR']
count=df['Dept'].value_counts()
#           ************* PIE CHART *************  #When data consists non numerical values

# plt.pie(count,labels=count.index,autopct="%0.1f",explode=[0,0.1,0])
# print(plt.show())
# print(df.info())

#       ****************** BAR CHART *****************
# plt.bar(count.index,count)
# print(plt.show())

df['Age']=[22,30,24,25,28,22,26,24,23,28]
#  ******* BIVARIATE DAAT *********

#       ********** SCATTER PLOT ************
# plt.scatter(df['Age'],df['Salary'])
# print(plt.show())   

sort_age=df.sort_values('Age')
# plt.plot(sort_age['Age'],df['Salary'],color='blue')
# print(plt.show())


#   PLOTTING MULTIPLE BOX IN BOX MODEL ( A CATEGORICAL AND ONE NUMERICAL)
df_hr=df[df['Dept']=='HR']['Salary']
df_fin=df[df['Dept']=='Finance']['Salary']
df_sal=df[df['Dept']=='Sales']['Salary']

# plt.boxplot([df_hr,df_sal,df_fin],tick_labels=["HR","Sales","Finance"])
# print(plt.show())

#   CATIGORICAL AND NUMERICAL USING PYCHART 

# sum_by_dept=df.groupby('Dept')['Salary'].sum()
# plt.pie(sum_by_dept,labels=sum_by_dept.index,autopct='%1.2f')
# print(plt.show())

#       ********* BAR CHART **********
# hr_sal_mean=sum(df_hr)/len(df_hr)
# sales_sal_mean=sum(df_hr)/len(df_sal)
# fin_sal_mean=sum(df_hr)/len(df_fin)

# plt.bar(['HR','Sales','Finance'],['hr_sal_mean','sales_sal_mean','fin_sal_mean'])
# print(plt.show())


df['experience']=[1,2,3,4,5,5,4,3,2,1]
#           ******* BUBBLE PLOT *******
### Three numerical data 

#       **** SCATTER PLOT ****

# #              rows, columns       s=size of bubble
# plt.scatter(df['Age'],df['Salary'],s=df['experience']*20,color='tomato')
# print(plt.show())

#       ******* SCATTER for 2 numerical one 1 categorical

# plt.scatter(df['Age'],df['Salary'],c=df['Dept'].map({'HR':'red','Sales':'blue','Finance':'yellow'}))
# print(plt.show())



#  #        ******** OBJECT - ORIENTED API ********

# fig , axs =plt.subplots(1,3, figsize=(10,4))

# #           ****** LINE PLOT ******
# axs[0].plot(sort_age['Age'],df['Salary'])      
# axs[0].set_title('Line graph')

# #           ****** HISTOGRAM ******

# axs[1].hist(df['Salary'],bins=5,color='red')
# axs[1].set_title('Histogram')

# #           ****** BOXPLOT ******

# axs[2].boxplot(df['Salary'])
# axs[2].set_title('Histogram')

# plt.savefig('multiple_plot.png')        # can save in our local env
# print(plt.show())


#           ***** MULTIPLE PLOT *****

data2={
    'Year':['2021','2022','2023','2024','2025'],
    'Sales':[100,50,150,100,250],
    'Profit':[10,20,30,20,10]
}

df2=pd.DataFrame(data2)
# plt.plot(df2['Year'],df2['Sales'],label='Sales')
# plt.plot(df2['Year'],df2['Profit'],label='Profit')

# plt.legend()
# print(plt.show())


# ********* 3-D PLOT ********

# ax=plt.axes(projection='3d')
# ax.scatter(df['Salary'],df['experience'],df['Age'])

# print(plt.show())