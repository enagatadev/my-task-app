# タスク管理アプリ

シンプルなWebベースのタスク管理アプリです。タスクの追加・削除・期限・優先度の管理ができます。

## 技術スタック

- **Python** 3.x
- **Flask** - Webフレームワーク
- **JSON** - データ保存

## 機能

- タスクの追加
- タスクの削除
- 期限の設定
- 優先度の設定（高 / 中 / 低）

## インストールと起動

### 1. リポジトリをクローン

```bash
git clone https://github.com/enagatadev/my-task-app.git
cd my-task-app
```

### 2. 仮想環境を作成・有効化

```bash
python -m venv venv

# Mac / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### 4. アプリを起動

```bash
python app.py
```

ブラウザで `http://localhost:5000` を開くと使えます。

## ライセンス

[MIT](LICENSE)
