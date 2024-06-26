from django.contrib import admin
from .models import Genre, Person, Filmwork, GenreFilmwork, PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified')
    list_filter = ('created',)
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created', 'modified')
    list_filter = ('created',)
    search_fields = ('full_name',)


class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline, )

    list_display = ('title', 'type', 'creation_date', 'rating',)
    list_filter = ('type', 'creation_date', 'rating',)
    search_fields = ('title', 'description', 'id')
