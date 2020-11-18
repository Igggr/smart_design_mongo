from flask import Blueprint, views
from flask import request, Response

from app.models import Goods

rst = Blueprint("rst", __name__, url_prefix="/goods")


class ApiView(views.MethodView):
    
    def post(self):
        body = request.get_json()
        good = Goods(**body).save()
        id = good.id
        return {'id': str(id)}, 200

    def delete(self):
        Goods.objects.delete()
        return 'ok', 200

    def get(self):
        goods = Goods.objects.to_json()
        return Response(goods, mimetype="application/json", status=200)


rst.add_url_rule("/", view_func=ApiView.as_view("goods"))

