# โครงการทดสอบ API

โครงการนี้ประกอบด้วย Flask API อย่างง่ายและชุดการทดสอบ

## โครงสร้างโครงการ

- `app.py`: Flask API อย่างง่ายที่มีเอ็นด์พอยต์ต่อไปนี้:
  - `POST /users`: สร้างผู้ใช้ใหม่
  - `GET /users/<user_id>`: ขอข้อมูลผู้ใช้ตาม ID
  - `DELETE /users/<user_id>`: ลบผู้ใช้ตาม ID
- `test_api.py`: การทดสอบ Pytest สำหรับ Flask API ที่รันบนเครื่อง
- `mockapitest.py`: การทดสอบ Pytest สำหรับ API จำลองภายนอก

## การติดตั้ง

1. **สร้างสภาพแวดล้อมเสมือน (virtual environment):**
   ```bash
   python -m venv .venv
   ```

2. **เปิดใช้งานสภาพแวดล้อมเสมือน:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **ติดตั้งสิ่งที่ต้องใช้ (dependencies):**
   ```bash
   pip install Flask requests pytest
   ```

## การรันแอปพลิเคชัน

1. **เริ่ม Flask API:**
   ```bash
   python app.py
   ```
   API จะทำงานที่ `http://127.0.0.1:5000`

## การรันการทดสอบ

1. **รันการทดสอบสำหรับ API บนเครื่อง:**
   ```bash
   pytest test_api.py
   ```

2. **รันการทดสอบสำหรับ API จำลอง:**
   ```bash
   pytest mockapitest.py
   ```