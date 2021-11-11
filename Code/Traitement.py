import numpy as np
import cv2 as cv
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
import matplotlib.pyplot as plt

class Traitement(object):
    
    def __init__(self):
        self.gaussianNB = GaussianNB(var_smoothing=0.9)
        self.bernoulliNB = BernoulliNB()
        self.multinomialNB = MultinomialNB()

        #Les sorties désirées pour notre exemples d'apprentissage
        self.d_learning = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'E',
                           'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'J', 'J',
                           'K', 'K', 'L', 'L', 'M', 'M', 'N', 'N', 'O', 'O', 'O', 'P', 'P',
                           'Q', 'Q', 'R', 'R','S', 'S', 'T', 'T','U', 'U', 'U', 'V', 'V',
                           'W', 'W', 'X', 'X', 'Y', 'Y', 'Z', 'Z']

        #Sorties du test
        self.d_test = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E',
                       'F', 'F', 'G', 'H', 'H', 'I', 'I', 'J', 'J',
                       'K', 'L', 'M', 'M', 'N', 'N', 'O', 'O', 'P', 'P',
                       'Q', 'R','S', 'S', 'T', 'U', 'U', 'V',
                       'W', 'X', 'Y', 'Z']
    
    #import_img() fonction qui fait des pre-traitements sur les images de nos exemples (apprentissage ou test)
    def import_img(self, phase, n):
        imgs = []
        for i in range(1, n):
            img = "D:/Master SIR/TAAD/TPs/TAAD_TP04_FIRASS_Mohammed/images/"+phase+"/".__add__(i.__str__()).__add__(".png")
            img = cv.imread(img)
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
            imgs.append(img.flatten())
        return imgs

    #apprentissage basee sur la methode fit() du naive_bayes
    def gaussian_learning(self):
        images = self.import_img('apprentissage', 63)
        self.gaussianNB.fit(images, self.d_learning)

    def bernoulli_learning(self):
        images = self.import_img('apprentissage', 63)
        self.bernoulliNB.fit(images, self.d_learning)

    def multinomial_learning(self):
        images = self.import_img('apprentissage', 63)
        self.multinomialNB.fit(images, self.d_learning)
    
    #faire des tests sur nos exemples du test/apprentissage et calculer le taux de reussite
    def gaussian_learning_success_rate(self):
        images = self.import_img('apprentissage', 63)
        count = 0
        for i in range(len(images)):
            result = self.gaussianNB.predict([images[i]])
            if result[0] == self.d_learning[i]:
                count += 1
        return format((count/62)*100, ".2f")

    def bernoulli_learning_success_rate(self):
        images = self.import_img('apprentissage', 63)
        count = 0
        for i in range(len(images)):
            result = self.bernoulliNB.predict([images[i]])
            if result[0] == self.d_learning[i]:
                count += 1
        return format((count/62)*100, ".2f")

    def multinomial_learning_success_rate(self):
        images = self.import_img('apprentissage', 63)
        count = 0
        for i in range(len(images)):
            result = self.multinomialNB.predict([images[i]])
            if result[0] == self.d_learning[i]:
                count += 1
        return format((count/62)*100, ".2f")


    def gaussian_test_success_rate(self):
        images = self.import_img('test', 42)
        count = 0
        for i in range(len(images)):
            result = self.gaussianNB.predict([images[i]])
            if result[0] == self.d_test[i]:
                count += 1
        return format((count/41)*100, ".2f")

    def bernoulli_test_success_rate(self):
        images = self.import_img('test', 42)
        count = 0
        for i in range(len(images)):
            result = self.bernoulliNB.predict([images[i]])
            if result[0] == self.d_test[i]:
                count += 1
        return format((count/41)*100, ".2f")

    def multinomial_test_success_rate(self):
        images = self.import_img('test', 42)
        count = 0
        for i in range(len(images)):
            result = self.multinomialNB.predict([images[i]])
            if result[0] == self.d_test[i]:
                count += 1
        return format((count/41)*100, ".2f")
    