#coding=utf8
from django.db import models
from Levenshtein import levenshtein_similarity
# from Manager.models import Commodity
import jieba
import difflib

class SearchEngine:
    catagory = ['运动鞋', '运动服饰', '体育用品', '骑行运动', '户外装备']

    def similarity(self, query_name, goods_name):
        if 1.0 * len(query_name) / len(goods_name) > 0.7:
            sim1 = difflib.SequenceMatcher(None, query_name, goods_name).quick_ratio()
        else:
            sim1 = 0

        query_name_list_zh = []
        goods_name_list_zh = []
        query_name_list_en = []
        goods_name_list_en = []
        repeated_zh = []
        repeated_en = []
        for each in jieba.cut(query_name):
            if each == ' ':
                continue
            if each.encode( 'UTF-8' ).isalpha(): #是否是英文
                query_name_list_en.append(each.lower())
            else:
                query_name_list_zh.append(each)
            
        for each in jieba.cut(goods_name):
            if each == ' ' or each.lower() in repeated_en or each in repeated_zh:
                continue
            if each.encode( 'UTF-8' ).isalpha(): #是否是英文
                goods_name_list_en.append(each.lower())
                repeated_en.append(each.lower())
            else:
                goods_name_list_zh.append(each)
                repeated_zh.append(each)

        result = 0.0
        count = 0
        #中文词比对
        for i in goods_name_list_zh:
            word_result = 0
            for j in query_name_list_zh:
                sim = difflib.SequenceMatcher(None, i, j).quick_ratio()
                if sim > 0:
                    word_result = word_result + sim
                    count += 1
                if sim:
                    print i + '' + j + ' ' + str(sim)
            # 每个词至要少有一个分数
            if i in query_name_list_zh: 
                word_result = 1 #如果单词在关键字中，则将相似度置为1
            
            if word_result == 0:
                count += 0.1 #如果该单词完全不相关，使分数降低一些
            else:
                result += word_result
            
        #英文词比对, 不计算相关度，而是考虑单词是否在商品名称中
        for i in goods_name_list_en:
            word_result = 0
            for j in query_name_list_en:
                if i == j:  #如果单词在关键字中，则将相似度置为1
                    word_result = 1.0
                    count += 1
            # 每个词至要少有一个分数
            if word_result == 0:
                count += 0.1 #如果该单词完全不相关，使分数降低一些
            else:
                result += word_result

        if count == 0:
            return 0
        else:
            result = result / count

        result = max(sim1, result)
        return result
