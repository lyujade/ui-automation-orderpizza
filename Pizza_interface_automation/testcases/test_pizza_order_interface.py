import pytest
from common.common_methods import *
url="http://localhost:3001/api/order"
size=["small","medium","large"]
ingredients=[["cheese"],["bacon"],["egg"],["cheese","bacon"],["cheese","egg"],["bacon","egg"],["cheese","bacon","egg"]]

class Testoderpizza():
    # order one pizza
    @pytest.mark.parametrize("size", size)
    @pytest.mark.parametrize("ingredient", ingredients)
    def test_one_pizza(self,size,ingredient):
        """order one pizza test cases"""
        doc = Testoderpizza.test_one_pizza.__doc__ + "site[{}]".format(str(url))+"size:%s,ingredient:%s"%(size,ingredient)
        orderId=get_orderId(url,doc)
        pizza_body={"pizzas": [{"size": size, "toppings":ingredient}],"orderId":orderId}
        post_orderId(url, pizza_body, doc)

    # order two pizzas
    @pytest.mark.parametrize("size1", size)
    @pytest.mark.parametrize("ingredient1", ingredients)
    @pytest.mark.parametrize("size2", size)
    @pytest.mark.parametrize("ingredient2", ingredients)
    def test_two_pizzas(self,size1,ingredient1,size2,ingredient2):
        """order two pizzas test cases"""  
        doc = Testoderpizza.test_one_pizza.__doc__ + "site[{}]".format(str(url))+"size1:%s,ingredient1:%s,size2:%s,ingredient2:%s"%(size1,ingredient1,size2,ingredient2)
        orderId = get_orderId(url, doc)
        pizza_body={"pizzas": [{"size": size1, "toppings":ingredient1},{"size": size2, "toppings":ingredient2}],"orderId":orderId}
        post_orderId(url, pizza_body, doc)

    # order three pizzas
    @pytest.mark.parametrize("size1", size)
    @pytest.mark.parametrize("ingredient1", ingredients)
    @pytest.mark.parametrize("size2", size)
    @pytest.mark.parametrize("ingredient2", ingredients)
    @pytest.mark.parametrize("size3", size)
    @pytest.mark.parametrize("ingredient3", ingredients)
    def test_three_pizzas(self, size1, ingredient1, size2, ingredient2,size3,ingredient3):
        """order three pizzas test cases"""
        doc = Testoderpizza.test_one_pizza.__doc__ + "site[{}]".format(str(url)) + "size1:%s,ingredient1:%s,size2:%s,ingredient2:%s,size3:%s,ingredient3:%s"%(size1,ingredient1,size2,ingredient2,size3,ingredient3)
        orderId = get_orderId(url, doc)
        pizza_body = {"pizzas": [{"size": size1, "toppings": ingredient1}, {"size": size2, "toppings": ingredient2}, {"size": size3, "toppings": ingredient3}],
                      "orderId": orderId}
        print('{"size": %s, "toppings":%s},{"size": %s, "toppings":%s}' % (size1, ingredient1, size2, ingredient2))
        post_orderId(url, pizza_body, doc)






