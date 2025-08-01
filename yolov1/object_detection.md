---
title: "Object Detection Series"
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

Introduction to Object Detection
===

Youtube Link: [Object Detection Series](./https://www.youtube.com/playlist?list=PLhhyoLH6Ijfw0TpCTVTNk42NN08H6UvNq)

### Goals:
- Understand what Object Detections is about and how it works
- Get an overview of the historical progress with different models
- Intersection over Union
- Non max suppression
- Mean Average Precision
- Yolo Algorithm from scratch
<!-- end_slide -->

Introduction
===

Object Localization is finding what and where a (single) object exists in an image.

Object Detection is finding what and where (multiple) objects are in an image.

So how do we do Object Localization ? 

Alright, so localization is no biggie !

But... how dow we generalize this for multiple objects in an image ?

There are many approaches to solving object detection and each is in many ways unique.

![](./notes_ss/localization.png)


<!-- end_slide -->


**Sliding Windows** : The `natural` extension
![](./notes_ss/sliding_window_.png)
Note: The sliding window is usually a square.

*Potential Problems*:
- A Lot of Computation
- Many bounding boxes for the same object

<!-- end_slide -->

### Regional Based Networks:

![](./notes_ss/region_based_networks.png)

*Problems*:
- Still slow and complicated, 2 step process

<!-- end_slide -->

Yolo: You Look Only Once
===

![](./notes_ss/yolo.png)

<!-- end_slide -->

Intersection Over Union
===

How do we measure how good a bounding box is ?
- First Calculate Intersection
- Second, calculate Union

### Metric: Intersection over Union (IoU)

IoU = Area Of Intersection / Area of Union      -> [0,1] 

![](./notes_ss/iou.png)

![](./notes_ss/iou2.png)


<!-- end_slide -->

![](./notes_ss/iou3.png)

![](./notes_ss/iou_formula.png)