import os
from os import listdir
from django.shortcuts import render
import re

# Create your views here.
def home_view(request):
	return render(request,'home.html',{})

def about_view(request):
	return render(request,'about.html',{}) 

def contact_view(request):
	return render(request,'contactus.html',{})

def abs_summarize(request):
	Path = './static/dataset/abs_summarize'
	lis = [folder for folder in listdir(Path)]
	params = {'List_of_dirs':lis,'dataset' : 'abs_summarize'}
	return render(request,'dataset.html',params)

def ext_summarize(request):
	Path = './static/dataset/ext_summarize'
	lis = [folder for folder in listdir(Path)]
	params = {'List_of_dirs':lis, 'dataset' : 'ext_summarize'}
	return render(request,'dataset.html',params)

def squad_dataset(request):
	Path = './static/dataset/squad_dataset'
	lis = [folder for folder in listdir(Path)]
	params = {'List_of_dirs':lis, 'dataset' : 'squad_dataset'}
	return render(request,'dataset2.html',params)

def odqa_dataset(request):
	Path = './static/dataset/odqa_dataset'
	lis = [folder for folder in listdir(Path)]
	params = {'List_of_dirs':lis, 'dataset' : 'odqa_dataset'}
	return render(request,'dataset2.html',params)

def get_articles(request,dataset,folder_path):
	path = "./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="abs_summarize"):
		lis= [folder for folder in listdir(path)]
	elif(dataset=="ext_summarize"):
		lis = [folder.split('.')[0] for folder in listdir(path+"input")]
	elif(dataset=="odqa_dataset"):
		lis = [folder for folder in listdir(path)]
	elif(dataset=="squad_dataset"):
		lis=[folder for folder in listdir(path)]
	content ={
		'folder' : folder_path,
		'list_folders' : lis,
		'dataset' : dataset,
	}
	return render(request,'articles.html',content)

def get_articles2(request,dataset,folder_path):
	path = "./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="odqa_dataset"):
		lis = [folder for folder in listdir(path)]
	elif(dataset=="squad_dataset"):
		lis=[folder for folder in listdir(path)]
	content ={
		'folder' : folder_path,
		'list_folders' : lis,
		'dataset' : dataset,
	}
	return render(request,'articles2.html',content)


def get_contents(request,dataset,folder_path,article):
	path= "./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="abs_summarize"):
		lis= [folder for folder in listdir(path)]
	elif(dataset=="ext_summarize"):
		lis = [folder.split('.')[0] for folder in listdir(path+"input")]
	elif(dataset=="odqa_dataset"):
		lis = [folder for folder in listdir(path)]
	elif(dataset=="squad_dataset"):
		lis=[folder for folder in listdir(path)]
	
	org_article = sum_article=""

	if(dataset=='abs_summarize'):
		org_article=os.path.join(path,article)+"/article."+article+".txt"
		sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	elif(dataset=='ext_summarize'):
		org_article= path+"/input/"+article+".txt"
		sum_article=path+"/output/"+article+"_out.txt"
	#elif(dataset=='odqa_dataset'):
		#org_article=os.path.join(path,article)+article+".checked"
		#sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	#elif(dataset=='squad_dataset'):
		#org_article=os.path.join(path,article)+"/article."+article+".txt"
		#sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	

	f=open(org_article,"r",encoding="utf-8")
	org_content=f.read()
	f.close()

	f=open(sum_article,"r",encoding="utf-8")
	sum_content=f.read()
	f.close()

	content={
		'article_id': article,
		'article' : org_content,
		'summary' : sum_content,
		'folder' : folder_path,
		'list_folders' : lis,
		'dataset' : dataset,
	}
	return render(request,'articles.html',content)


def get_contents2(request,dataset,folder_path,article):
	path= "./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="odqa_dataset"):
		org_article = os.path.join(path,articles)+article+"labeled.txt"
		with open ("org_article", "r", encoding="utf-8") as fp:
			data = fp.readlines()
			num = len(data)
			lis = [folder for folder in range(1,num)]
	#elif(dataset=="squad_dataset"):
		#lis=[folder for folder in listdir(path)]
	
	org_article = sum_article=""

	if(dataset=='odqa_dataset'):
		ques = os.path.join(path,articles)+article+"question.txt"
		ans = os.path.join(path,articles)+article+"answer.txt"
		label = os.path.join(path,articles)+article+"label.txt"

	f=open(ques,"r",encoding="utf-8")
	ques1=f.read()
	f.close()

	f=open(ans,"r",encoding="utf-8")
	ans1=f.read()
	f.close()

	f=open(label,"r",encoding="utf-8")
	label1=f.read()
	f.close()


	#elif(dataset=='squad_dataset'):
		#org_article=os.path.join(path,article)+"/article."+article+".txt"
		#sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	

	"""f=open(org_article,"r",encoding="utf-8")
	org_content=f.read()
	ques = []
	ans = []
	label = []
	pattern1 = r'[A-Z](3)'
	label = re.findall(pattern1,org_content)
	pattern2 = r'].*?'
	ques = re.findall(pattern2,org_content)
	pattern3 = r'[@](3)*'
	ans = re.findall(pattern3,org_content)
	f.close()"""

	content={
		'question':ques1,
		'answer':ans1,
		'label' :label1,
		'folder' : folder_path,
		'list_folders' : lis,
		'dataset' : dataset,
	}
	return render(request,'articles2.html',content)
