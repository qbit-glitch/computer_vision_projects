---
title: "YOLOv3"
author: Umesh Kumar Singh
theme: 
    name: gruvbox-dark
    override :
        footer:
            style: progress_bar
            # left: "My **name** is {author}"
            # center: "_@qbit_glitch_"
            right: "{current_slide} / {total_slides}"
            height: 1
        slide_title:
            padding_bottom: 0
            padding_top: 0
            separator: true
        headings:
            h1:
                prefix: "██"
            h2:
                prefix: "▓▓▓"
        code:
            theme_name: base16-ocean.dark
    image_protocol: kitty-local
    typst:
        ppi: 400
    
    typst:
        colors:
            background: ff0000
            foreground: 00ff00

        # In points
        horizontal_margin: 2
        vertical_margin: 2
---

Implement YOLOv3 from scratch
===

YT Link: [YOLOv3 from scratch](https://youtu.be/Grir6TZbc1M)

In addition to [x,y,w,h] each box also has probability that there exists an object in the cell and class predictions.