import numpy as np
from flask import Flask, render_template, request
from 代码.data_predict import model

app = Flask(__name__)


# 加载机器学习模型和相关的预处理函数

def predict(age, gender, chest_pain, blood_sugar, rest_ecg, exercise_angina, exercise_st, thalassemia, cholesterol, blood_pressure, max_heart_rate, st_depression, vessels):
    # 定义一个一行25列的矩阵
    test_data = np.empty(25, dtype=object)
    # 设置1-4个元素为int型
    test_data[:4] = np.random.randint(1, 10, 4)
    # 设置5-6个元素为float型
    test_data[4:6] = np.random.rand(2)
    # 设置剩余元素为bool型
    test_data[6:] = np.random.choice([True, False], size=19)
    test_data[0] = age
    test_data[1] = blood_pressure
    test_data[2] = cholesterol
    test_data[3] = max_heart_rate
    test_data[4] = st_depression
    test_data[5] = vessels

    if gender == '男':
        test_data[6] = False
        test_data[7] = True
    else:
        test_data[6] = True
        test_data[7] = False

    if chest_pain == '典型心绞痛':
        test_data[8:12] = [True, False, False, False]
    elif chest_pain == '无心绞痛':
        test_data[8:12] = [False, True, False, False]
    elif chest_pain == '渐进式疼痛':
        test_data[8:12] = [False, False, True, False]
    else:
        test_data[8:12] = [False, False, False, True]

    if blood_sugar == '大于120mg/dl':
        test_data[12:14] = [True, False]
    else:
        test_data[12:14] = [True, False]

    if rest_ecg == '左心室肥大':
        test_data[14:17] = [True, False, False]
    elif rest_ecg == '患有ST-T波异常':
        test_data[14:17] = [False, True, False]
    else:
        test_data[14:17] = [False, False, True]

    if exercise_angina == '否':
        test_data[17:19] = [True, False]
    else:
        test_data[17:19] = [False, True]

    if exercise_st == '下降':
        test_data[19:22] = [True, False, False]
    elif exercise_st == '平缓':
        test_data[19:22] = [False, True, False]
    else:
        test_data[19:22] = [False, False, True]

    if thalassemia == '可逆缺陷':
        test_data[22:25] = [True, False, False]
    elif thalassemia == '固定缺陷':
        test_data[22:25] = [False, True, False]
    else:
        test_data[22:25] = [False, False, True]

    print(test_data)
    test_data = np.array(test_data).reshape(1, -1)
    result1 = model.predict(test_data)
    result2 = model.predict_proba(test_data)

    return result1, result2

def interpret_result(result):
    # Interpret the prediction result
    if result == [0]:
        return "预测结果为:   没有患心脏病"
    elif result == [1]:
        return "预测结果为:   患有心脏病"


def interpret_proba_result(result):
    probability_no_heart_disease = result[0][0]
    probability_heart_disease = result[0][1]
    return f"其中：\n患心脏病概率: {probability_heart_disease:.2%} \n不患心脏病概率: {probability_no_heart_disease:.2%}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    age = int(request.form['age'])
    blood_pressure = int(request.form['blood_pressure'])
    cholesterol = int(request.form['cholesterol'])
    max_heart_rate = int(request.form['max_heart_rate'])
    st_depression = float(request.form['st_depression'])
    vessels = float(request.form['vessels'])
    gender = request.form['gender']
    chest_pain = request.form['chest_pain']
    blood_sugar = request.form['blood_sugar']
    rest_ecg = request.form['rest_ecg']
    exercise_angina = request.form['exercise_angina']
    exercise_st = request.form['exercise_st']
    thalassemia = request.form['thalassemia']

    result1, result2 = predict(age, gender, chest_pain, blood_sugar, rest_ecg, exercise_angina, exercise_st, thalassemia, cholesterol, blood_pressure, max_heart_rate, st_depression, vessels)

    print(result1)
    print(result2)
    interpretation1 = interpret_result(result1)
    interpretation2 = interpret_proba_result(result2)

    return render_template('result.html', interpretation1=interpretation1, interpretation2=interpretation2)

if __name__ == '__main__':
    app.run(debug=True)

