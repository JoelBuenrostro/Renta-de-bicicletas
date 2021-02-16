from flask import Flask, render_template, flash, request, jsonify, Markup

INTERCEPT = -121.029547
COEF_HOLIDAY = -23.426176
COEF_HOUR = 8.631624
COEF_SEASON_1 = 3.861149
COEF_SEASON_2 = -1.624812
COEF_SEASON_3 = -41.245562
COEF_SEASON_4 = 39.009224
COEF_TEMP = 426.900259

MEAN_HOLIDAY = 0
MEAN_HOUR = 11.6
MEAN_SEASON_1 = 0

MEAN_SEASON_2 = 0
MEAN_SEASON_3 = 1
MEAN_SEASON_4 = 0
MEAN_TEMP = 0.4967

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html',
                           mean_holiday=MEAN_HOLIDAY,
                           mean_hour=MEAN_HOUR,
                           mean_season1=MEAN_SEASON_1,
                           mean_season2=MEAN_SEASON_2,
                           mean_season3=MEAN_SEASON_3,
                           mean_season4=MEAN_SEASON_4,
                           mean_temp=MEAN_TEMP,
                           model_intercept=INTERCEPT,
                           model_holiday=COEF_HOLIDAY,
                           model_hour=COEF_HOUR,
                           model_season1=COEF_SEASON_1,
                           model_season2=COEF_SEASON_2,
                           model_season3=COEF_SEASON_4,
                           model_temp=COEF_TEMP)


if __name__ == '__main__':
    app.run(debug=True)
