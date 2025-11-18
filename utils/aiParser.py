def yolo_result_parser(result, labels):
    parsed_results = []
    boxes = result[0].boxes

    for box in boxes:
        cls_id = int(box.cls.cpu().numpy()[0])
        conf = float(box.conf.cpu().numpy()[0])
        x1, y1, x2, y2 = box.xywh.cpu().numpy()[0].tolist()

        parsed_results.append({
            "class_id": cls_id,
            "confidence": conf,
            "bounding_box": (x1, y1, x2, y2),
            "label": labels[cls_id] if labels and cls_id < len(labels) else None
        })

    return parsed_results