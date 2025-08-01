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

<!-- end_slide -->

Non-Max Suppression Algorithm
===

Perhaps start with discarding all bounding boxes < `probaility threshold`.

While BoundingBoxes:
- take out the largest probability box
- Remove all other boxes with IoU > threshold 

(And we do this for each class)

![](./notes_ss/nms.png)

<!-- end_slide -->

Mean Average Precision
===
Goal is to understand and implement the most common metric used in Deep Learning to evaluate object detection models.

Concretely after this video, if we read `"mAP@0.5:0.05:0.95"` in a research paper, we should know exactly what that means, and know how to do that evaluation on our own model.

Steps:
1. Get all the bounding box predictions on our test set.
2. Sort by descending confidence score.
3. Calculate the Precision and Recall as we go through all outputs.
4. Plot the Precision-Recall graph.
5. Calculate area under the Precision Recall Curve.
6. This was only for one class, we need to calculate for all classes. 


![](./notes_ss/mAP.png)

<!-- end_slide -->

![](./notes_ss/mAP2.png)
![](./notes_ss/mAP3.png)
![](./notes_ss/mAP4.png)

<!-- end_slide -->

Precision and Recall
===

![](./notes_ss/precision_recall.png)
There's a battle between precision and recall! Different applications may prioritize recall and others precision.

<!-- end_slide -->

- Cat AP = 0.74
- Dog AP = 0.533

mAP = (0.533 + 0.74)/2 = 0.6365

7. All of this was calculates given a specific IoU threshold of 0.5, 0.55, 0.6, ... , 0.95. Then average this and this will be our final result. This is what is meant by `mAP@0.5:0.05:0.95` 
 