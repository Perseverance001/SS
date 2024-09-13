cursor.execute("insert into DRES values(%s,%s,%s,%s,%s,%s,%s,%s)",
               (2, 10001, 'UDparameter/predict_parameter.txt', now, 'predicted_images', 'predicted_images', '', ''))
conn.commit()
#获取检测的批次
cursor.execute("SELECT IDENT_CURRENT('DRES')")
row = cursor.fetchone()
id = row[0]
for image_dbase in image_path:
    img = image_dbase
    try:
        image = Image.open(img)
        # 读取保存地址里面图片的编号

        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg'))]
        # 如果文件夹为空，初始命名为1，否则找到当前文件夹中最大的数字并加1
        if len(image_files) == 0:
            max_number = 1
        else:
            existing_numbers = [int(os.path.splitext(os.path.basename(file))[0]) for file in image_files]
            max_number = max(existing_numbers) + 1
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = ssd.detect_image(image, crop=crop, count=count)
        r_image.show()
        file_extension = os.path.splitext(os.path.basename(img))[1]
        new_filename = str(max_number) + file_extension
        file_path = os.path.join(folder_path, new_filename)
        r_image.save(file_path)

        print(id, new_filename, file_path)
        #保存单张图的检测的批次、、检测之后图片的路径
        #第二个参数是预测图的原图编号，在图形化界面获取
        cursor.execute("insert into DIMG values(%s,%s,%s)",
                       (id, '0001-01-01', file_path))
        conn.commit()