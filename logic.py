import math
SHAPES = {
    "สี่เหลี่ยมผืนผ้า": (
        ["กว้าง", "ยาว"],
        "พื้นที่ = กว้าง × ยาว",
        lambda w, l: w * l,
    ),
    "สี่เหลี่ยมจัตุรัส": (
        ["ด้าน"],
        "พื้นที่ = ด้าน²",
        lambda s: s ** 2,
    ),
    "สามเหลี่ยม": (
        ["ฐาน", "สูง"],
        "พื้นที่ = ½ × ฐาน × สูง",
        lambda b, h: 0.5 * b * h,
    ),
    "วงกลม": (
        ["รัศมี"],
        "พื้นที่ = π × รัศมี²",
        lambda r: math.pi * r ** 2,
    ),
    "สี่เหลี่ยมด้านขนาน": (
        ["ฐาน", "สูง"],
        "พื้นที่ = ฐาน × สูง",
        lambda b, h: b * h,
    ),
    "สี่เหลี่ยมคางหมู": (
        ["ด้านคู่ขนานที่ 1", "ด้านคู่ขนานที่ 2", "สูง"],
        "พื้นที่ = ½ × (ด้านคู่ขนาน 1 + ด้านคู่ขนาน 2) × สูง",
        lambda a, b, h: 0.5 * (a + b) * h,
    ),
    "วงรี": (
        ["แกนเอก (ครึ่งหนึ่ง)", "แกนโท (ครึ่งหนึ่ง)"],
        "พื้นที่ = π × a × b  (a, b คือความยาวครึ่งแกน)",
        lambda a, b: math.pi * a * b,
    ),
    "สามเหลี่ยมมุมฉาก": (
        ["ฐาน", "สูง"],
        "พื้นที่ = ½ × ฐาน × สูง",
        lambda b, h: 0.5 * b * h,
    ),
    "สี่เหลี่ยมขนมเปียกปูน": (
        ["เส้นทแยงมุมที่ 1", "เส้นทแยงมุมที่ 2"],
        "พื้นที่ = ½ × เส้นทแยงมุม 1 × เส้นทแยงมุม 2",
        lambda d1, d2: 0.5 * d1 * d2,
    ),
}


def shape_names():
    return list(SHAPES)


def get_fields(name):
    return SHAPES[name][0]


def get_formula(name):
    return SHAPES[name][1]


def calculate_area(name, values):
    if name not in SHAPES:
        raise ValueError("ไม่พบรูปทรงที่เลือก")
    if len(values) != len(get_fields(name)):
        raise ValueError("กรุณาใส่ตัวเลขให้ครบทุกช่อง")
    if any(not math.isfinite(v) or v <= 0 for v in values):
        raise ValueError("กรุณากรอกตัวเลขที่มากกว่า 0")
    return SHAPES[name][2](*values)