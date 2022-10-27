from fastapi import FastAPI, Form
from fastapi.params import Body
app = FastAPI()
app.add_api_route('/', index)
app.add_api_route('/{user}', admin, methods=['GET', 'POST'])
app.add_api_route('/time_depart', register, methods=['GET', 'POST'])
app.add_api_route('/time_depart//time_depart/{depart_stop}/{depart_pos}/{arrival_stop}/{arrival_pos}/{depart_year}/{depart_month}/{depart_day}/{depart_hour}/{depart_minutes}/{prepare_minutes}/{arrival_year}/{arrival_month}/{arrival_day}/{arrival_hour}/{arrival_minutes}}/{arrival_allow_minutes}', detail)
