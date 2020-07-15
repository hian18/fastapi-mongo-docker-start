from bs4 import BeautifulSoup
# import re

# ava = open(
#     "view-source_https___ceadvirtual.mrooms.net_course_view.php_id=26574#section-4.html"
# )
# soup = BeautifulSoup(ava, "html.parser")


# contents = soup.find_all("div", {"class": "content"})

# view = []
# semanas = {}


# def set_html(semana, titulo, link):
#     if semana in semanas:
#         semanas[semana] += f'<p>{titulo}</p><p><a href="{link}">{link}</a></p>'
#     else:
#         semanas[
#             semana
#         ] = f'<hr><p>{semana}</p><p>{titulo}</p><p><a href="{link}">{link}</a></p>'


# for c in contents:
#     rows = c.find_all("div", {"class": "no-overflow"})
#     for r in rows:
#         medias = r.find_all("div", {"class": "mediaplugin mediaplugin_videojs"})
#         for media in medias:
#             try:

#                 if media:
#                     titulo = r.table.text.strip("\n").strip(" ")
#                     link = ""
#                     a = media.div.video.attrs.get("data-setup-lazy", None)
#                     semana = c.div.h2.text
#                     if a:
#                         for x in re.findall(r"https:\/\/youtu\.be\/\w+", a):
#                             link = x

#                             set_html(semana, titulo, link)
#                             break

#             except Exception as ex:
#                 titulo = r.p.text.strip("\n").strip(" ")
#                 link = ""
#                 a = media.div.video.attrs.get("data-setup-lazy", None)
#                 if a:
#                     for x in re.findall(r"https:\/\/youtu\.be\/\w+", a):
#                         link = x
#                         semana = c.div.h2.text
#                         set_html(semana, titulo, link)
#                         break

# for x in semanas:
#     print(semanas[x])
import pdfkit

pdfkit.from_file("vander.html", "vander.pdf")

