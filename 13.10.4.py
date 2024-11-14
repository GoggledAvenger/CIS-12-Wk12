import os, hashlib

def is_image(file_path,extensions):
    if not os.path.isfile(file_path): return False
    root, ext = os.path.splitext(file_path)
    return ext in extensions

def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

def add_path(file_path,db):
    key = md5_digest(file_path)
    if key in db:
        if file_path not in db[key]:
            db[key].append(file_path)
    else:
        db[key] = [file_path]
    return db

def walk_images(directory, extensions, db):
    for root, dirs, files in os.walk(directory, topdown=True):
        for file in files:
            file = os.path.join(root, file)
            if is_image(file,extensions):
                add_path(file,db)

def same_contents(path1, path2):
    data1 = open(path1, 'rb').read()
    data2 = open(path2, 'rb').read()
    return data1 == data2

def main():
    extensions = ['.png','.jpg','.jpeg', '.tiff','.gif']
    #print(is_image('photos/feb-2023/photo1.jpg',extensions))
    db = {}
    walk_images('photos',extensions, db)

    for digest, paths in db.items():
        if len(paths) > 1:
            print(same_contents(*paths))

if __name__ == '__main__':
    main()
