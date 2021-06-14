from django.shortcuts import render
from django.http import HttpResponse, response
import pandas as pd
import numpy as np
import xlwt
from django.contrib.auth.models import User

emopsP = pd.read_csv("C:/Users/oscar.ribeiro/Desktop/streamlit cob/dadosEMOPsPreco.csv", sep=';', error_bad_lines= False,warn_bad_lines=False)


# def index(request):
#      df=emopsP.transpose().iloc[4:].reset_index()
#      df.columns=["ID_empresa","CODIGO","Descr_codigo","UNID"]
#      allData=[]
#      for i in range(df.shape[0]):
#           temp=df.loc[i]
#           allData.append(dict(temp))
#      context= {'data':allData}
#      return render(request,'COBTEST.html',context)



# Create your views here.

# def home(request):
#     return render(request, 'home.html', {'name':'Oscar'});

# def add(request):

#     val1 = int(request.POST['num1']) #Sem i int() o programa reconhece os valores como string
#     val2 = int(request.POST['num2'])
#     res = val1 + val2


#     return render(request, 'result.html', {'result':res})


def home(request):
     return render(request, 'COBTEST.html');


# def export_csv(request):
#      response = HttpResponse(content_type="text/csv")
#      response['Content-Dosposition'] = 'attachment; filename=Expenses' + \ 
#      str(datetime.datetime.now())+ '.csv'

#      writer = csv.writer(response)
#      write.writerow(["Amount",'Description','Category',"Date"])
     
#      expenses = Expenses.objects.filter(owner=resquet.user)

#      for expense in expenses:
#           write.writerow([expense.amount, expense.description, 
#           expense.category, expense.date])



#      return response

# def export_excel(request):
#      response = HttpResponse(content_type='application/ms-excel')
#      response['Content-Dosposition'] = 'attachment; filename="users.xls"'

#      wb = xlwt.workbook(encoding='utf-8')
#      ws=wb.add_sheet('Users') #tabela
#      row_num= 0

#      font_style= xlwt.XFStyle()
#      font_style.font.bold = True

#      columns = ["Amount",'Description','Category',"Date"] #Inserir os nomes das colunas

#      for col_num in range(len(columns)):
#           ws.write(row_num, col_num, columns[col_num], font_style)
     
#      font_style= xlwt.XFStyle()

#      rows = User.objects.all().values_list()#nomes colunas
#      for row in rows:
#           row_num += 1
#           for col_num in range(len(row)):
#                ws.write(row_num,col_num,row[col_num],font_style)

# def create(request):
#     voteTypeForm = VoteTypeForm(request.POST or None)
#     voteForm = VoteForm(request.POST or None)
#     if request.method == 'POST':
#         # check validity separately to avoid short-cutting
#         vote_type_valid = voteTypeForm.is_valid()
#         vote_form_valid = voteForm.is_valid()
#         if vote_type_valid and vote_form_valid:
#             instance = voteTypeForm.save(commit=False)
#             instance.pub_date = timezone.now()
#             instance.save()
#             instance2 = voteForm.save(commit=False)
#             instance2.save()
#             return redirect('<view-you-redirect-to-on-success'>
#     context = RequestContext(request,{
#             'voteTypeForm': voteTypeForm,
#             'voteForm': voteForm,
#     })
#     return render(request, 'Vote/create.html', context)

# Inserir dados
def selecionardados():
     emop2 = emopsP.query()


# Remover linha 
def removerlinha():
     emop2.drop(x) 


# Zerar tabela
def excluirtabela():
     emop2 = emop2[0:0]


# exportar para Excel
def exportExcel (): 
#     global emop2 
    pd.ExcelWriter('DadosOrcamento.xlsx')
#     export_file_path = filedialog.asksaveasfilename (defaultextension = '. xlsx') 
#     emop2.to_excel (export_file_path, index = False, header = True)
