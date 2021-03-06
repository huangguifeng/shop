from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, HiddenField, \
    SelectField, StringField, BooleanField
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.validators import DataRequired


# 修改会员信息表单
class UserDetailForm(FlaskForm):
    image = FileField(
        label="头像",
        validators=[
            DataRequired("请上传头像"),
            FileAllowed(['jpg', 'png', 'jpeg', 'gif', 'bmp'], "只能上传图片！"),
            FileRequired("文件未选择！"),
        ],
        description="头像",
    )
    info = TextAreaField(
        label='简介',
        validators=[
            DataRequired("请输入简介")
        ],

        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10,

        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={"class": "btn btn-success  ", }
    )


# 添加评论记录
class CommentForm(FlaskForm):
    content = TextAreaField(
        label='评论',
        validators=[
            DataRequired("请输入评论信息")

        ],
        description="评论",
        render_kw={
            "class": "form-control",
            "rows": 10,
        }
    )
    comment_good_id = IntegerField(
        label='商品ID',
        description="",
        render_kw={
            "class": "form-control",
            "rows": 10,
        }
    )
    submit = SubmitField(
        '提交评论',
        render_kw={"class": "btn btn-success  ", }
    )


# 购物车选中商品去结算
class Buy(FlaskForm):
    pass


# 添加收货地址表单
class AddAddress(FlaskForm):
    # 省份
    province = SelectField()
    # 城市
    city = SelectField()
    # 地区
    area = SelectField()
    # 详细地址
    address = StringField()
    # 联系电话
    phone = StringField()
    # 姓名
    name = StringField()
    # 备注
    remarks = StringField()
    # 是否设置为默认地址
    default_add = BooleanField()
    # 提交数据
    submit = SubmitField(
        '提交',
        render_kw={"class": "btn btn-success  ", }
    )
