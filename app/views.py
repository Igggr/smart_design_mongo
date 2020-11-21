from flask import Blueprint, views
from flask import request, Response, abort

from app.models import Goods

rst = Blueprint("rst", __name__, url_prefix="/goods")


class GoodsApiView(views.MethodView):

    def post(self):
        body = request.get_json()
        # print(request.json)
        good = Goods(**body).save()
        uid = good.id
        return {'id': str(uid)}, 200

    def delete(self):
        Goods.objects.delete()
        return 'ok', 200

    def get(self):
        goods = Goods.objects
        # print(request.args)
        if request.args:
            for key, val in request.args.items():
                # print(f"{key}: {val}")
                if key == "name":
                    goods = goods.filter(name=val)
                elif key == "description":
                    goods = goods.filter(description=val)
                else:  # filter by keys-value stored in parameters
                    goods = goods.filter(__raw__={f"parameters.{key}":  {'$exists': True}})  # has such key
                    goods = goods.filter(__raw__={f"parameters.{key}": val})                 # and it has right value
        return Response(goods.to_json(), mimetype="application/json", status=200)


class SingleGoodApiView(views.MethodView):

    def get(self, uid):
        good = Goods.objects.with_id(object_id=uid)
        if not good:
            abort(404)
        else:
            return Response(good.to_json(), mimetype="application/json", status=200)


rst.add_url_rule("/", view_func=GoodsApiView.as_view("goods"))
rst.add_url_rule("/<uid>", view_func=SingleGoodApiView.as_view("good"))
