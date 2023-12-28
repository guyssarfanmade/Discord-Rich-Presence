
# วิธีการใช้งานของ Rich Presence

- เพิ่อที่จะใช้งานต้องทำการติดตั้ง Discord RPC Library สำหรับ Python

```bash
  pip install pypresence
```
- หลังจากติดตั้ง Library  เสร็จแล้วแก้ไขไฟล์ตามที่ต้องการ 
    - เข้าไป [DEVELOPER PORTAL](https://discord.com/developers/applications) และไปที่ `Applications` เลือกบอทที่ต้องการ ในหน้า `General Information` คัดลอก `APPLICATION ID` มาเติมใน `เติม APPLICATION ID`

   ```bash 
   client_id = 'เติม APPLICATION ID'
   ```
    - เข้าไป [DEVELOPER PORTAL](https://discord.com/developers/applications) และไปที่ `Rich Presence` และไปหน้า `Visualizer` คัดลอก `PARTY ID` มาเติมใน `เติม party_id`
   ```bash 
   'party_id': 'เติม party_id'
   ```
    - อื่นๆแก้ไขตามที่ต้องการได้เลย
- หลังจากแก้ไขเสร็จแล้วใช้คำสั่ง (เลือกใช้งาน)
```bash
  python {FileName}.py
```
```bash
  python3 python {FileName}.py
```

