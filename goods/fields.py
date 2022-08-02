import os
from PIL import Image
from django.db.models import ImageField   # 이미지 필드
from django.db.models.fields.files import ImageFieldFile   # 이미지저장 파일(?)


class ThumbnailImageFieldFile(ImageFieldFile):
    def _add_thumb(self, s):
        parts = s.split('.')   # 파일명 때문에 . 으로 잘라줌
        parts.insert(-1, 'thumb')   # 원본 파일 이름을 변경 뒤에 thumb 붙임 (원본하고 구분하기 위해(?))
        if parts[-1].lower() not in ('jpeg', 'jpg'):
            parts[-1] = 'jpg'
        return '.'.join(parts)   # 확장자를 .jpg로 통일

    @property
    def thumb_path(self):
        return self._add_thumb(self.path)

    @property
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self, name, content, save=True):
        super().save(name, content, save)   # super() -> 더 상위 개념에게 request보냄?(엄마! 나 이거 해줘!)
                                            # 원본을 save
        img = Image.open(self.path)         # 여기부터 썸네일 만들어서 저장할꺼
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0]-img.size[0])/2), int((size[1]-img.size[1])/2))
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG')   # PIL 기본형식이 jpeg일 가능성이 높음.(jpg를 사용해도 될껄)

    def delete(self, save=True):    # 저장이 되어있으면 지움
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)   # 부모에게 지워달라고 요청


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super().__init__(verbose_name, **kwargs)
