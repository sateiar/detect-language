from tesserocr import PyTessBaseAPI
import tesserocr
import numpy as np
images = [r"C:\Users\Farshid\Desktop\New folder (3)\rental march - april.PNG"]
def detect_lang(image):
    flag_autorization = True
    language_list =tesserocr.get_languages()[1]

    listarr= []
    listsumarr = []
    # a= []

        # api.SetImageFile(images[0])
    for lang in language_list:
        try :
            with PyTessBaseAPI() as api:
                api.SetImageFile(image)
                api.Init(lang = lang,oem = tesserocr.OEM.LSTM_ONLY)
                # a.append(api.GetUTF8Text())
                listarr.append(list(api.AllWordConfidences()))
                listsumarr.append(sum(listarr[-1]) / float(len(listarr[-1])))
                print()
        except:
            print()

    if max(listsumarr) > 50 :
        score1=listsumarr[(np.array(listsumarr)).argmax()]
        langfinal=language_list[(np.array(listsumarr)).argmax()]
        if langfinal !='eng' and listsumarr[(np.array(listsumarr)).argmax()] - listsumarr[language_list.index('eng')] < 5:
            langfinal=langfinal+'+eng'

    else:
        langfinal='eng'
        flag_autorization = False
    print('detect language: '+str(langfinal))
    return langfinal,flag_autorization
detect_lang(images[0])


#
# n = min([len(i) for i in listarr])
# result = []
# for i in range(0 , n):
#     temp =[]
#     for j in range(len(listarr)):
#         temp.append(listarr[j][i])
#     mint = np.array(temp).min()
#     if len ([a for a in temp if a == mint ] ) == 1 :
#         result.append(np.array(temp).argmin())
#     ## count
# final=language_list[np.array([result.count(idx) for idx in range(len(listarr))]).argmax()]
# score=listsumarr[np.array([result.count(idx) for idx in range(len(listarr))]).argmax()]
# print('langauge:',final)
# print('score: ',score)
#
#     # a = min(temp)
#     # print()
#
# # print (n)