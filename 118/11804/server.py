from flask import Flask, render_template, jsonify, url_for
import os

app = Flask(__name__)

# 一定要在這裡定義 VALID_EXTS，才能在函式裡使用
VALID_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}

@app.route('/api/images')
def api_images():
    images_dir = os.path.join(app.static_folder, 'images')
    try:
        filenames = os.listdir(images_dir)
    except FileNotFoundError:
        return jsonify(images=[])
    
    images = []
    for fname in filenames:
        full = os.path.join(images_dir, fname)
        ext = os.path.splitext(fname)[1].lower()
        # 濾掉非檔案、非圖片
        if os.path.isfile(full) and ext in VALID_EXTS:
            # 產生瀏覽器可用的 URL (預設 static_folder 是 ./static)
            images.append(url_for('static', filename=f'images/{fname}'))
    # 方法一：直接 print 到 stdout
    print("DEBUG - images list:", images)    
    return jsonify(images=images)

@app.route('/')
def index():
    # 自動取得 static 資料夾中所有圖片
    image_folder = os.path.join('static')
    images = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)