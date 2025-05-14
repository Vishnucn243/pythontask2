import pandas as pd
data = {
    'name':['ann','athira','athul','abhay'],
    'salary':[100,200,300,400],
    'experience':[1,4,3,3],
    'place':['kochi','alappy','kannur','calicut']
}
df=pd.DataFrame(data)
df.to_excel("excelcontent.xlsx", index=False)

def fun(file_path):
    df=pd.read_excel(file_path)
    summary=df.describe()
    return summary

result=fun("excelcontent.xlsx")
print(result)
