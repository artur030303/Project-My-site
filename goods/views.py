from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

from django.core.paginator import Paginator


# Create your views here.
def catalog(request) -> HttpResponse:
    context = {
        "goods": [
            {
                "image": "source1/images/moto/moto01/moto1.jpg",
                "name": "HARLEY-DAVIDSON Electra Glide 2011",
                "mileage": "Пробег: 258 км.",
                "description": "Electra Glide, называемый в народе «электричка",
                "full_description": "Первый Electra Glide, называемый в народе «электричка», сошел с конвейера еще в 1965 году. С тех пор эта модель считается одной из самых востребованных. Но несмотря на то, что эталон байка для туризма, казалось, уже был достигнут, Harley-Davidson не перестает удивлять своих поклонников.",
                "price": "11.200",
                "image_slide1": "source1/images/moto/moto01/moto1.1",
                "image_slide2": "source1/images/moto/moto01/moto1.2",
                "image_slide3": "source1/images/moto/moto01/moto1.3",
                "id": "carouselMoto1",
            },
            {
                "image": "source1/images/moto/moto2/moto1.jpg",
                "name": "HARLEY-DAVIDSON V-ROD RED 2003",
                "mileage": "Пробег: 3582 км.",
                "description": "Юбилейная модель VRSCA V-Rod",
                "full_description": "Юбилейная модель VRSCA V-Rod вышла в 2003 году. Онабыла основана на двигателе спортбайка VR1000, которыйимелся на ней в модифицированной версии – онвырабатывал 115 лошадиных сил максимальной мощности,что на 20 лошадиных сил меньше, чем оригинальнаяверсия данного силового агрегата. Кроме того, егорабочий объём возрос до 1130 куб. см. Двигательпредставлял собой 4-тактный 2-цилиндровый 8-клапанныйагрегат с двумя распредвалами в головке цилиндра ижидкостным охлаждением. Он работал со степенью сжатия11,3:1. Электронная система впрыска топлива имела53-миллиметровые дроссельные заслонки. Максимальныйкрутящий момент составлял 88 Нм на 6300 об/мин.",
                "price": "12.000",
                "image_slide1": "source1/images/moto/moto2/moto1.1",
                "image_slide2": "source1/images/moto/moto2/moto1.2",
                "image_slide3": "source1/images/moto/moto2/moto1.3",
                "id": "carouselMoto2",
            },
            {
                "image": "source1/images/moto/moto3/moto1.jpg",
                "name": "HARLEY-DAVIDSON Dyna Glide 2005",
                "mileage": "Пробег: 1238 км.",
                "description": "Модель FXDC Dyna Super Glide Custom",
                "full_description": "В 2005 году вышла модель FXDC Dyna Super Glide Custom,которая приводилась в движение двигателем Twin Cam 96.Он представлял собой верхнеклапанный 4-тактныйV-образный силовой агрегат с двумя цилиндрами. Диаметрцилиндра составлял 95,25 мм, а ход поршня – 111,25 мм.Рабочий объём двигателя был равен 1584 куб. см.Охлаждение двигателя осуществлялось воздухом. Степеньсжатия составляла 9,2:1. Мотоцикл имел инжекторнуютопливную систему ESPFI. Он был оборудован6-скоростной трансмиссией с ремённым приводом.Передаточные числа: 1-я 9.312 9.312 9.030 / 2-я 6.4216.421 6.266 / 3-я 4.774 4.774 4.630 / 4-я 3.926 3.9263.807 / 5-я 3.279 3.279 3.179 / 6-я 2.790 2.790 2.706.Максимальный крутящий момент составлял 124,7 Нм на3000 об/мин. Система подвески была представленаалюминиевой вилкой с 49-миллиметровыми перьями, атакже задним пружинным амортизатором.",
                "price": "8.600",
                "image_slide1": "source1/images/moto/moto3/moto1.1",
                "image_slide2": "source1/images/moto/moto3/moto1.2",
                "image_slide3": "source1/images/moto/moto3/moto1.3",
                "id": "carouselMoto3",
            },
            {
                "image": "source1/images/moto/moto4/moto1.jpg",
                "name": "HARLEY-DAVIDSON Electra Glide 2000",
                "mileage": "Пробег: 390 км.",
                "description": "Electra Glide, называемый в народе «электричка",
                "full_description": " Первый турер Electra Glide, называемый в народе«электричка», сошел с конвейера еще в 1965 году. С техпор эта модель считается одной из самыхвостребованных. Но несмотря на то, что эталон байкадля туризма, казалось, уже был достигнут,Harley-Davidson не перестает удивлять своихпоклонников. Хотя внешне живое воплощение классики запоследние тридцать лет почти не изменилось, этовпечатление обманчиво. Под винтажным обликом ElectraGlide скрывается один из самых продуманных и надежныхмотоциклов. Неудивительно, что вокруг него возникцелый культ, а в мире есть немаломoтoпутешественников, которые совершили на этом байкекругосветную поездку.",
                "price": "9.800",
                "image_slide1": "source1/images/moto/moto4/moto1.1",
                "image_slide2": "source1/images/moto/moto4/moto1.2",
                "image_slide3": "source1/images/moto/moto4/moto1.3",
                "id": "carouselMoto4",
            },
            {
                "image": "source1/images/moto/moto5/moto1.jpg",
                "name": "BMW S 1000 RR supersport B, 2024",
                "mileage": "Пробег: 12258 км.",
                "description": "Этот мотоцикл создан для новых рекордов",
                "full_description": "Этот мотоцикл создан для новых рекордов. 207 лошадиныхсил и 113 Нм крутящего момента при 13,500 об/мин –причем более 100 Нм доступно в диапазоне от 5,500 до14,500 об/мин. Спустя десять лет после премьеры RRпервого поколения мы вновь переписываем правила вклассе спортбайков. Новый S 1000 RR создан с чистоголиста. Он намного легче и мощнее. Он – новый эталон.Вы готовы всегда быть на первом месте? Тогда новый RRсоздан для вас.",
                "price": "11.900",
                "image_slide1": "source1/images/moto/moto5/moto1.1",
                "image_slide2": "source1/images/moto/moto5/moto1.2",
                "image_slide3": "source1/images/moto/moto5/moto1.3",
                "id": "carouselMoto5",
            },
            {
                "image": "source1/images/moto/moto6/moto1.jpg",
                "name": "VESPA Primavera  scooter orange, 2021 ",
                "mileage": "Пробег: 8 км.",
                "description": "Спортивный вариант скутера Веспа",
                "full_description": " Спортивный вариант скутера Веспа ― Примавера 150 С.Удивительно, но в таком небольшом высокопрочномстальном кузове спрятан настоящий спортивный характер.Убедитесь в этом сами, отправившись в дорогу наэлегантном мотороллере с экономичным ипроизводительным двигателем объемом 150 см³. Моторразвивает мощность 12,9 л.с., удивляя низким уровнемвыбросов и фантастически маленьким расходом топлива израсчета 1 литр на 43,2 км. При этом максимальнаяскорость Primavera 150 S может достигать 95 км/час!Качество и надежность двигателей Vespa известны вовсем мире, моторы действительно по многим параметрамопережают свое время.",
                "price": "1.000",
                "image_slide1": "source1/images/moto/moto6/moto1.1",
                "image_slide2": "source1/images/moto/moto6/moto1.2",
                "image_slide3": "source1/images/moto/moto6/moto1.3",
                "id": "carouselMoto6",
            },
        ]
    }
    goods = context["goods"]
    paginator = Paginator(goods, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "goods/catalog.html", {"page_obj": page_obj})


def product(request):
    return render(request, "goods/product.html")
