# NOTE

Chưa có bản tin cài đặt cảnh cho các thiết bị :Màn hình, socket, switch, IR

# TABLE OF CONTENTS

- THÔNG TIN THIẾT BỊ VÀ THUỘC TÍNH
  - BẢNG THUỘC TÍNH THIẾT BỊ
  - DANH SÁCH PHÂN LOẠI THIẾT BỊ
- BẢN TIN ĐIỀU KHIỂN
  - DEVICE
  - GROUP
  - SCENE
  - DEVICE UPDATE
  - CẢM BIẾN
  - SCENE CONTROLLER
  - BATTERY
- BẢN TIN CẤU HÌNH
  - DEVICE
  - GROUP
  - SCENE
  - SCENE CONTROLLER
  - SCENE - SENSOR
  - SCENE - SCREEN
  - EVENT TRIGGER
  - HCL
  - COUNTDOWN
  - PHÒNG
  - CẤU HÌNH HC
  - CÁC THIẾT BỊ SMART HOME
- BẢN TIN KHÁC
  - ĐIỀU HOÀ
  - QUẠT / TV
  - IR DEVICES

# THÔNG TIN THIẾT BỊ VÀ THUỘC TÍNH

## BẢNG THUỘC TÍNH THIẾT BỊ

| ID  | CODE                | NAME                            | Range      | Data Type  |
| :-- | :------------------ | :------------------------------ | :--------- | :--------- |
| 0   | STATUS              | Trạng thái bật / tắt            | 0, 1       | Bit        |
| 1   | DIM                 | Độ sáng                         | 0 - 100    | Percentage |
| 2   | CCT                 | Nhiệt độ màu                    | 0 - 100    | Percentage |
| 3   | HUE                 | Giá trị Hue                     | 0 - 65535  | Integer    |
| 4   | SATURATION          | Giá trị Saturation              | 0 - 65535  | Integer    |
| 5   | LUMINANCE           | Giá trị Luminance               | 0 - 65535  | Integer    |
| 6   | SONG                | Bài hát                         | 1 - n      | Integer    |
| 7   | BLINK_MODE          | Chế độ nháy theo nhạc           | 1 - 10     | Integer    |
| 8   | BATTERY             | Phần trăm PIN                   | 1 - 100    | Percentage |
| 9   | LUX                 | Độ sáng đo được                 | 0 - 83865  | Integer    |
| 10  | PIR                 | Trạng thái cảm biến             | 0, 1       | Bit        |
| 11  | BUTTON_1            | Nút số 1                        | 0 - 2      | Integer    |
| 12  | BUTTON_2            | Nút số 2                        | 0 - 2      | Integer    |
| 13  | BUTTON_3            | Nút số 3                        | 0 - 2      | Integer    |
| 14  | BUTTON_4            | Nút số 4                        | 0 - 2      | Integer    |
| 15  | BUTTON_5            | Nút số 5                        | 0 - 2      | Integer    |
| 16  | BUTTON_6            | Nút số 6                        | 0 - 2      | Integer    |
| 17  | ACTIME              | Thời gian giữ trạng thái        | 0 - 65535  | Integer    |
| 18  | PM2.5               | Bụi mịn 2.5                     | 0-999      | Integer    |
| 19  | PM10                | Bụi mịn 10                      | 0-999      | Integer    |
| 20  | PM1.0               | Bụi mịn 1.0                     | 0-999      | Integer    |
| 21  | TEMP                | Nhiệt độ                        | -199 - 999 | Integer    |
| 22  | HUMIDITY            | Độ ẩm                           | 0 - 100    | Integer    |
| 23  | SCENE_RGB           | Giá trị cảnh RGB mặc định       | 1 - 6      | Integer    |
| 24  | HANGON              | Trạng thái treo lên hay không   | 0, 1       | Bit        |
| 25  | FAN_OFF             | Tắt quạt                        | 0-255      | Integer    |
| 26  | FAN_ON              |                                 | 0-255      | Integer    |
| 27  | FAN_SPEED           |                                 | 0-255      | Integer    |
| 28  | FAN_SWING           |                                 | 0-255      | Integer    |
| 29  | FAN_MODE            |                                 | 0-255      | Integer    |
| 30  | TV_ON/OFF           |                                 | 0-255      | Integer    |
| 31  | TV_MUTE             |                                 | 0-255      | Integer    |
| 32  | TV_SOUND_UP         |                                 | 0-255      | Integer    |
| 33  | TV_SOUND_DOWN       |                                 | 0-255      | Integer    |
| 34  | TV_CHANNEL_UP       |                                 | 0-255      | Integer    |
| 35  | TV_CHANNEL_DOWN     |                                 | 0-255      | Integer    |
| 36  | OK                  |                                 | 0-255      | Integer    |
| 37  | UP                  |                                 | 0-255      | Integer    |
| 38  | DOWN                |                                 | 0-255      | Integer    |
| 39  | LEFT                |                                 | 0-255      | Integer    |
| 40  | RIGHT               |                                 | 0-255      | Integer    |
| 41  | NUM_0               |                                 | 0-255      | Integer    |
| 42  | NUM_1               |                                 | 0-255      | Integer    |
| 43  | NUM_2               |                                 | 0-255      | Integer    |
| 44  | NUM_3               |                                 | 0-255      | Integer    |
| 45  | NUM_4               |                                 | 0-255      | Integer    |
| 46  | NUM_5               |                                 | 0-255      | Integer    |
| 47  | NUM_6               |                                 | 0-255      | Integer    |
| 48  | NUM_7               |                                 | 0-255      | Integer    |
| 49  | NUM_8               |                                 | 0-255      | Integer    |
| 50  | NUM_9               |                                 | 0-255      | Integer    |
| 51  | AIR_CONDITION_MODE  |                                 | 0 - 4      | Integer    |
| 52  | AIR_CONDITION_FAN   |                                 | 0 - 5      | Integer    |
| 53  | AIR_CONDITION_SWING |                                 | 0 - 5      | Integer    |
| 54  | BTN_OPEN            | Nút mở rèm                      | 0, 1       | Bit        |
| 55  | BTN_CLOSE           | Nút đóng rèm                    | 0, 1       | Bit        |
| 56  | BTN_PAUSE           | Nút tạm dừng                    | 0, 1       | Bit        |
| 57  | OPENED              | Phần trăm giá trị mở của rèm    | 1-100      | Integer    |
| 58  | SMOKE               | Giá trị có khói / không có khói | 0, 1       | Bit        |
| 59  | DOOR                | Giá trị mở / đóng của cửa       | 0, 1       | Bit        |

## DANH SÁCH PHÂN LOẠI THIẾT BỊ

### Category

- Là nhóm các thiết bị có cùng tính năng kĩ thuật, đánh mã dạng số nguyên có 2 chữ số
- Các thiết bị trong cùng category hỗ trợ cùng một tập thuộc tính.
  Ví dụ: Đèn LED vàng trắng (CCT) (12) hỗ trợ các thuộc tính:
- Điều khiển trạng thái bật / tắt
- Điều khiển độ sáng
- Điều khiển nhiệt độ màu

### DeviceType

- Là một loại thiết bị đặc trưng theo hình thức thiết kế, đánh mã dạng số nguyên 5 chữ số
- 2 chữ số đầu trong mã thiết bị, là mã category
  Ví dụ:
- Đèn LED Downlight SMT (12001) là một loại đèn CCT

### Bảng phân loại

| ID  | CODE  | NAME                                            | Mã BLE   |
| :-- | :---- | :---------------------------------------------- | :------- |
| 1   | 12001 | Đèn LED Downlight SMT                           | 01:02:01 |
| 2   | 12002 | Đèn LED Downlight COB góc rộng (>60 độ)         | 01:02:02 |
| 3   | 12003 | Đèn LED Downlight COB góc hẹp (chiếu trang trí) |          |
| 4   | 12004 | Đèn LED Downlight COB trang trí (AT19.BLE)      |          |
| 5   | 12005 | Đèn LED Panel tròn                              |          |
| 6   | 12006 | Đèn LED Panel Vuông, chữ nhật, Troffer          |          |
| 7   | 12007 | Đèn LED Ốp trần                                 |          |
| 8   | 12008 | Đèn LED Ốp tường                                |          |
| 9   | 12009 | Đèn LED chiếu tranh gắn tường                   |          |
| 10  | 12010 | Đèn LED Tracklight                              | 01:02:0A |
| 11  | 12011 | Đèn LED Thả trần                                |          |
| 12  | 12012 | Đèn LED chiếu gương                             |          |
| 13  | 12013 | Đèn LED Dây CCT, Linear trang trí               |          |
| 14  | 12014 | Đèn LED Tube, M16                               |          |
| 15  | 12015 | Đèn Bàn                                         |          |
| 16  | 12016 | Đèn LED Flooding và trang trí khác              |          |
| 17  | 14001 | Đèn LED dây RGBCW LD01.BLE.RGBCW                |          |
| 18  | 14002 | Đèn LED Bulb A60.BLE.RGBCW                      |          |
| 19  | 15001 | Đèn LED ốp trần loa đổi màu LN23.BLE.RGBCW      |          |
| 20  | 21001 | Bộ công tắc chuyển mạch CT.BLE ON/OFF           |          |
| 21  | 22001 | Công tắc cảm ứng RD-CT.01.BLE                   | 02:02:01 |
| 22  | 22004 | Công tắc cảm ứng RD-CT.04.BLE                   |          |
| 23  | 23001 | Bộ điều khiển cảnh (Pin) SC.M2 (DC)             |          |
| 24  | 23002 | Bộ điều khiển cảnh âm tường RD-SC03 (AC)        |          |
| 25  | 31001 | Bộ cảm biến ánh sáng CB03.LS.BLE                |          |
| 26  | 32001 | Cảm biến chuyển động - ánh sáng CB02.PIR.BLE    |          |
| 27  | 37001 | Bộ cảm biến bụi mịn                             |          |
| 28  | 22002 | Công tắc cảm ứng RD-CT.02.BLE                   |          |
| 29  | 22003 | Công tắc cảm ứng RD-CT.03.BLE                   |          |
| 30  | 22005 | Công tắc cảm ứng RD-CT.01.BLE.NL (CSC)          |          |
| 31  | 26001 | Ổ cắm đơn                                       |          |
| 32  | 26002 | Ổ cắm kéo dài                                   |          |
| 33  | 33001 | Bộ cảm biến khói                                |          |
| 34  | 36001 | Bộ cảm biến cửa                                 |          |
| 35  | 38001 | Cảm biến nhiệt độ, độ ẩm                        |          |
| 36  | 41001 | Bộ điều khiển hồng ngoại                        |          |
| 37  | 41101 | Quạt IR                                         |          |
| 38  | 41201 | TV IR                                           |          |
| 39  | 41301 | Điều hòa IR                                     |          |

# BẢN TIN ĐIỀU KHIỂN

Các bản tin điều khiển dành cho thiết bị, nhóm và cảnh

## Quy ước chung

- Các giá trị HSL là số nguyên trong khoảng 0..65535
- Các giá trị thuộc tính DIM, CTl quy về phần trăm 0..100
- Giá trị thời lượng PIN quy về phần trăm 0..100
- Giá trị độ sáng LUX của cảm biến
- Giá trị chuyển động PIR:
- Các chế độ nhấn và button ID là số nguyên và quy định riêng cho từng thiết bị

## Table of contents

- DEVICE
- GROUP
- SCENE
- DEVICE UPDATE
- CẢM BIẾN
- SCENE CONTROLLER
- BATTERY

## DEVICE

Mẫu bản tin điều khiển thiết bị

1. Json mẫu

Điều khiển một thiết bị có ID b717f8d8-6f18-43c0-ae46-69c32998f653, thiết lập giá trị cho thuộc tính có ID = 0 thành 1

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 0,
        "VALUE": 1
      }
    ]
  }
}
```

2. Bản tin phản hồi

Giống bản tin gửi đi nhưng được gửi vào topic phản hồi

## GROUP

Mẫu bản tin điều khiển theo nhóm

1. Json mẫu

App gửi lệnh điều khiển nhóm có ID=b717f8d8-6f18-43c0-ae46-69c32998f653, thiết lập giá trị thuộc tính ID = 0 thành 1 cho tất cả các thiết bị trong nhóm

```json
{
  "CMD": "GROUP",
  "DATA": {
    "GROUP_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 0,
        "VALUE": 1
      }
    ]
  }
}
```

2. Json phản hồi

Là bản tin phản hồi của điều khiển thiết bị:

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 0,
        "VALUE": 1
      }
    ]
  }
}
```

## SCENE

Mẫu bản tin điều khiển cảnh

1. Json mẫu

Kích hoạt cảnh có ID = aa3549d4-5471-4d75-b0b2- b70fa5c10fb2

```json
{
  "CMD": "SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Bản tin phản hồi

Bản tin phản hồi cho biết thiết bị đã nhận được lệnh kích hoạt cảnh

```json
{
  "CMD": "SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653"
  }
}
```

## DEVICE UPDATE

Các bản tin cập nhật trạng thái thiết bị từ HC

### Khi mở APP

1. Json mẫu

Gửi bản tin yêu cầu báo cáo trạng thái của các thiết bị tính từ thời điểm cập nhật cuối cùng TIME_UPDATE

```json
{
  "CMD": "DEVICE_UPDATE",
  "TIME_UPDATE": "YYYY MM D HH:MM"
}
```

2. Json phản hồi

Bản tin phản hồi với các thiết bị đang hoạt động

```json
{
  "CMD": "DEVICE_UPDATE",
  "DATA": [
    {
      "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
      "PROPERTIES": [
        {
          "ID": 0,
          "VALUE": 1
        },
        {
          "ID": 1,
          "VALUE": 100
        }
      ]
    }
  ]
}
```

Bản tin phản hồi trạng thái với các thiết bị OFFLINE

```json
{
  "CMD": "DEVICE_UPDATE_STATUS",
  "DATA": [
    {
      "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
      "STATUS": "OFFLINE"
    },
    {
      "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb3",
      "STATUS": "OFFLINE"
    }
  ]
}
```

## CẢM BIẾN

Các bản tin phản hồi của cảm biến sử dụng chung định dạng với bản tin phản hồi trạng thái của thiết bị thông thường.
Bạn có thể tra cứu ID của các thuộc tính tại BẢNG THUỘC TÍNH THIẾT BỊ.

### Cảm biến nhiệt độ - độ ẩm

Bản tin phản hồi giá trị nhiệt độ và độ ẩm đo được

- Nhiệt độ tính theo độ Celsius
- Độ ẩm tính theo phần trăm 0..100

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 21,
        "VALUE": 100
      },
      {
        "ID": 22,
        "VALUE": 100
      }
    ]
  }
}
```

### Cảm biến bụi mịn

Giá trị bụi mịn tính theo ppm

### Cảm biến ánh sáng

Bản tin phản hồi giá trị ánh sáng đo được

- Giá trị độ sáng do được: 0.83865`

### Cảm biến chuyển động

Bản tin phản hồi giá trị PIR đo được

- Giá trị chuyển động: 0 / 1 tương ứng với KHÔNG / CÓ chuyển động

### Cảm biến khói

Bản tin phản hồi giá trị khói đo được

- Giá trị khói: 0 / 1 tương ứng với KHÔNG / CÓ khói
  Bản tin phản hồi trạng thái PIN

- Giá trị pin của cảm biến khói: 0 / 1 tương ứng với PIN YẾU / PIN ĐẦY

### Cảm biến cửa

- Giá trị treo: 0 / 1, tương ứng với việc cảm biến KHÔNG / CÓ được gắn lên cửa
- Giá trị trạng thái cửa: 0 / 1, tương ứng với việc cửa đang MỞ / ĐÓNG
- Trạng thái cửa chỉ có ý nghĩa khi giá trị treo là 1

## SCENE CONTROLLER

### Trạng thái nút nhấn

```json
{
  "CMD": "REMOTE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "BUTTON_VALUE": "BUTTON_1",
    "MODE_VALUE": 1
  }
}
```

## BATTERY

Bản tin phản hồi trạng thái pin

- Giá trị POWER_VALUE: tính theo 0..100%

```json
{
  "CMD": "POW_STATUS",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "POWER_VALUE": 30
  }
}
```

# BẢN TIN CẤU HÌNH

Các bản tin cấu hình

- DEVICE
- GROUP
- SCENE
- SCENE CONTROLLER
- SCENE - SENSOR
- SCENE - SCREEN
- EVENT TRIGGER
- HCL
- COUNTDOWN
- PHÒNG
- CẤU HÌNH HC
- CÁC THIẾT BỊ SMART HOME

## DEVICE

### Quét thiết bị

1. Json mẫu

Bắt đầu quét thiết bị đưa vào mạng

```json
{
  "CMD": "SCAN"
}
```

2. Json phản hồi

Đề xuất:

- Bổ sung thêm địa chỉ MAC và phiên bản firmware thiết bị phục vụ cho monitoring trên web
- Đổi command từ TYPE_DEVICE thành NEW_DEVICE

```json
{
  "CMD": "NEW_DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d86f1843c0ae4669c32998f653",
    "DEVICE_UNICAST_ID": 2,
    "DEVICE_TYPE_ID": 23002,
    "MAC_ADDRESS": "AB:DE:EF",
    "FIRMWARE_VERSION": "1.0.2",
    "DEVICE_KEY": "b717f8d86f1843c0ae4669c32998f653",
    "NET_KEY": "b717f8d86f1843c0ae4669c32998f653",
    "APP_KEY": "b717f8d86f1843c0ae4669c32998f653"
  }
}
```

### Dừng quét

1. Json mẫu

Dừng quá trình đưa thiết bị vào mạng

```json
{
  "CMD": "STOP"
}
```

2. Json phản hồi
   HC thông báo việc dừng quét thiết bị

```json
{
  "CMD": "STOP"
}
```

### Xoá thiết bị ra khỏi mạng

1. Json mẫu

Xóa một danh sách thiết bị trong mạng theo ID. Từng thiết bị sẽ phản hồi về sau khi xóa khỏi mạng BLE

```json
{
  "CMD": "RESET_NODE",
  "DATA": [
    "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "b717f8d8-6f18-43c0-ae46-69c32998f654"
  ]
}
```

2. Json phản hồi

Đề xuất: Phản hồi lại danh sách các thiết bị xoá được và không xoá được theo từng trạng thái

```json
{
  "CMD": "RESET_NODE",
  "DATA": {
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

## GROUP

Các bản tin tạo nhóm sẽ được tối ưu:

- Bỏ trường TYPE và điều chỉnh các command cho từng trường hợp: tạo nhóm, thêm thiết bị, xoá thiết bị, xoá nhóm
- Sau khi nhóm được tạo thành công, app luôn gửi kèm unicast id xuống cho HC dùng nếu cần. Tuy nhiên, hai nhóm cần làm việc để đảm bảo luồng này hoạt động hợp lý và HC cần check trường hợp bị NULL để tránh crash chương trình
- Nếu HC cần giá trị Unicast ID cho những bản tin sau thì cần gửi lại GROUP_UNICAST_ID trong bản tin phản hồi tạo nhóm thành công
- Trong các bản tin phản hồi khác, HC có thể gửi kèm GROUP_UNICAST_ID để bản tin được thống nhất. Tuy nhiên app sẽ không sử dụng giá trị này.
- Nếu unicast ID bị null, APP cần bỏ trường đó ra khỏi bản tin để tránh lỗi cho HC

### Tạo nhóm

1. Json mẫu

Tạo một nhóm mới với một danh sách ID thiết bị
Nếu không có thiết bị thì trường sẽ để trống: "DEVICE": []

```json
{
  "CMD": "CREATE_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "DEVICE_TYPE_ID": 12001,
    "NAME": "abc",
    "DEVICES": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

2. Json phản hồi

HC trả về thông tin nhóm được tạo thành công và danh sách thiết bị được tạo thành công / thất bại.

```json
{
  "CMD": "CREATE_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152,
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

### Thêm thiết bị vào nhóm

1. Json mẫu

Thêm một danh sách thiết bị vào nhóm

```json
{
  "CMD": "ADD_DEVICE_TO_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152,
    "DEVICES": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

2. Json phản hồi

```json
{
  "CMD": "ADD_DEVICE_TO_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152,
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

### Xóa thiết bị khỏi nhóm

1. Json mẫu

Xoá một danh sách thiết bị khỏi nhóm

```json
{
  "CMD": "REMOVE_DEVICE_FROM_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152,
    "DEVICES": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

2. Json phản hồi

```json
{
  "CMD": "REMOVE_DEVICE_FROM_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152,
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

### Xoá nhóm

1. Json mẫu

Xoá toàn bộ nhóm

```json
{
  "CMD": "DELETE_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152
  }
}
```

2. Json phản hồi

```json
{
  "CMD": "DELETE_GROUP",
  "DATA": {
    "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "GROUP_UNICAST_ID": 49152,
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

## SCENE

Các bản tin tạo cảnh sẽ được tối ưu:

- Bỏ trường TYPE và điều chỉnh các command cho từng trường hợp: tạo cảnh, thêm thiết bị, xoá thiết bị, xoá cảnh
- Sau khi cảnh được tạo thành công, app luôn gửi kèm SCENE_UNICAST_ID xuống cho HC dùng nếu cần. Tuy nhiên, hai nhóm cần làm việc để đảm bảo luồng này hoạt động hợp lý và HC cần check trường hợp bị NULL để tránh crash chương trình
- Nếu HC cần giá trị Unicast ID cho những bản tin sau thì cần gửi lại SCENE_UNICAST_ID trong bản tin phản hồi tạo cảnh thành công
- Trong các bản tin phản hồi khác, HC có thể gửi kèm SCENE_UNICAST_ID để bản tin được thống nhất. Tuy nhiên app sẽ không sử dụng giá trị này.
- Nếu unicast ID bị null, APP cần bỏ trường đó ra khỏi bản tin để tránh lỗi cho HC
- Khi tạo scene, các thiết bị cùng loại sẽ được gom nhóm vào thành một object với một danh sách id để giảm thiểu việc lặp lại của danh sách properties

### Tạo cảnh thông thường

Trong trường hợp tạo cảnh thông thường, người dùng sẽ điều khiển đèn về trạng thái mong muốn trên APP nên HC không cần thực hiện việc này. HC chỉ cần đảm bảo việc gán cảnh đầy đủ cho danh sách đèn.
Chỉ được tạo một cảnh trong một bản tin

1. Json mẫu

```json
{
  "CMD": "CREATE_SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "DEVICES": [
      {
        "DEVICE_TYPE_ID": 12001,
        "IDS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "PROPERTIES": [
          {
            "ID": 0,
            "VALUE": 1
          },
          {
            "ID": 1,
            "VALUE": 100
          }
        ]
      }
    ]
  }
}
```

2. Json phản hồi

Sau thời gian timeout HC sẽ trả về cảnh nào vừa được cài đặt và trong cảnh đó có bao nhiêu thiết bị được cài thành công và bao nhiêu thiết bị thất bại.

```json
{
  "CMD": "CREATE_SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_UNICAST_ID": 2,
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

### Sửa cảnh thông thường

Tương tự khi tạo cảnh thông thường, HC vẫn nhận danh sách properties mới để lưu nhưng chỉ thực hiện lệnh gán cảnh cho đèn chứ không điều khiển.

1. Json mẫu

Khi sửa cảnh, app gửi lại danh sách các thiết bị thay đổi.
HC cần báo về trạng thái thực hiện cho từng thiết bị: SUCCESS hoặc FAILED
Bản tin này có thể được sử dụng cho việc "retry" khi có một hoặc nhiều thiết bị tạo cảnh thất bại

```json
{
  "CMD": "EDIT_SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "DEVICES": [
      {
        "DEVICE_TYPE_ID": 12001,
        "IDS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "PROPERTIES": [
          {
            "ID": 0,
            "VALUE": 1
          },
          {
            "ID": 1,
            "VALUE": 100
          }
        ]
      }
    ]
  }
}
```

1. Bản tin phản hồi
   HC gửi lại bản tin phản hồi thông báo cảnh đã được sửa và danh sách các thiết bị thành công và bị lỗi.

```json
{
  "CMD": "EDIT_SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_UNICAST_ID": 2,
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

### Xóa cảnh

1. Json mẫu

Khi xoá cảnh, app chỉ định ID cảnh được xoá.

```json
{
  "CMD": "DELETE_SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

Json phản hồi

HC gửi lại bản tin phản hồi với danh sách các thiết bị XOÁ ĐƯỢC và KHÔNG XOÁ ĐƯỢC, để app có cơ chế thử lại hoặc hiển thị cho người dùng biết và kiểm tra lại các đèn nếu cần.

```json
{
  "CMD": "DELETE_SCENE",
  "DATA": {
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SUCCESS": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ],
    "FAILED": [
      "b717f8d8-6f18-43c0-ae46-69c32998f653",
      "b717f8d8-6f18-43c0-ae46-69c32998f654"
    ]
  }
}
```

## SCENE CONTROLLER

### Gán cảnh cho scene controller

1. Json mẫu

Bản tin cần được tối ưu:

- Loại bỏ trường COMPARISON_OPERATOR_ID vì nó luôn là 1
- Loại bỏ trường DEVICE_ATTRIBUTE_ID vì nút nhấn đã được chỉ định trong - BUTTON_VALUE
- Loại bỏ trường EVENT_TRIGGER_TYPE_ID vì loại event trigger luôn là SCENE,
- Đổi tên EVENT_TRIGGER_ID thành SCENE_ID cho rõ nghĩa
  Ví dụ: Gán cảnh cho nút nhấn số 1 trên remote AC và DC, với "DEVICE_ID":"aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"

```json
{
  "CMD": "SCENE_FOR_REMOTE",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "BUTTON_VALUE": "BUTTON_1",
    "MODE_VALUE": 1,
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Json phản hồi

Giống bản tin gửi đi nhưng được gửi vào topic phản hồi

```json
{
  "CMD": "SCENE_FOR_REMOTE",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "BUTTON_VALUE": "BUTTON_1",
    "MODE_VALUE": 1,
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

### Xóa cảnh đã gán

1. Json mẫu

Bản tin cần được tối ưu:

- Bỏ trường TYPE và đổi câu lệnh thành DELETE_SCENE_FOR_REMOTE cho rõ nghĩa
- Các trường còn lại tối ưu giống với bản tin tạo
  Ví dụ:

```json
{
  "CMD": "DELETE_SCENE_FOR_REMOTE",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "BUTTON_VALUE": "BUTTON_1",
    "MODE_VALUE": 1,
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Json phản hồi

Giống bản tin gửi đi nhưng được gửi vào topic phản hồi

### Xoá toàn bộ cảnh được gán

1. Json mẫu

```json
{
  "CMD": "RESET_REMOTE",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Bản tin phản hồi

```json
{
  "CMD": "RESET_REMOTE",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

## SCENE - SENSOR

Bản tin cần được tối ưu:

- Bỏ trường TYPE và điều chỉnh các command cụ thể cho từng trường hợp
- Bỏ trường EVENT_TRIGGER_TYPE_ID vì lệnh luôn áp dụng cho cảnh
- Bỏ trường DEVICE_ATTRIBUTE_ID vì đã chỉ định cụ thể các giá trị cho LIGHT và PIR
- Bỏ trường COMPARISON_OPERATOR_ID vì đối với LIGHT thì luôn là chỉ định trong khoảng và với PIR thì luôn là một giá trị cụ thể
- PIR là 0 hoặc 1 tương ứng với KHÔNG / CÓ chuyển động
- Cú pháp với LUX: [LOW_VALUE, HIGH_VALUE]
- Nếu chỉ có giới hạn trên, tức phép toán nhỏ hơn hoặc bằng, set LOW_VALUE về -1
- Nếu chỉ có giới hạn dưới, tức phép toán lớn hơn hoặc bằng, set HIGH_VALUE về -1
- Nếu muốn chỉ định một giá trị cụ thể, set LOW_VALUE và HIGH_VALUE là cùng một giá trị
- Cách thiết kế này đã đủ cho nhu cầu sử dụng thông thường. Không hỗ trợ các phép toán quá phức tạp gây cho giá trị LUX gây khó hiểu cho người dùng.
- Bổ sung trường HANG_ON_TIME và AFTER_PIR_SCENE_ID để chọn thời gian chờ và cảnh được bật sau khi kết thúc chuyển động
- HANG_ON_TIME tính theo giây

### Gán cho cảm biến

1. Json mẫu

```json
{
  "CMD": "SCENE_FOR_SENSOR_LIGHT_PIR",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "LUX": [200, 600],
    "AFTER_PIR_SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Json phản hồi

Giống bản tin gửi đi nhưng có thêm trường EVENT_TRIGGER_ID để phục vụ sửa / xoá

```json
{
  "CMD": "SCENE_FOR_SENSOR_LIGHT_PIR",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "LUX": [200, 600],
    "AFTER_PIR_SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

### Sửa cảnh đã gán

1. Json mẫu

Đổi câu lệnh thành EDIT_SCENE_FOR_SENSOR_LIGHT_PIR

```json
{
  "CMD": "EDIT_SCENE_FOR_SENSOR_LIGHT_PIR",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "LUX": [200, 600],
    "AFTER_PIR_SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Json phản hồi

```json
{
  "CMD": "EDIT_SCENE_FOR_SENSOR_LIGHT_PIR",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "LUX": [200, 600],
    "AFTER_PIR_SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

### Xoá cảnh đã gán

1. Json mẫu

Đổi câu lệnh thành EDIT_SCENE_FOR_SENSOR_LIGHT_PIR

```json
{
  "CMD": "REMOVE_SCENE_FOR_SENSOR_LIGHT_PIR",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "AFTER_PIR_SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Json phản hồi

```json
{
  "CMD": "REMOVE_SCENE_FOR_SENSOR_LIGHT_PIR",
  "DATA": {
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "AFTER_PIR_SCENE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

## SCENE - SCREEN

- Bỏ trường TYPE và điều chỉnh câu lệnh tương ứng cho từng trường hợp
  Scene name tối đa 10 ký tự
- Bổ sung trường DEVICE_ID để HC biết gán cho thiết bị nào
- Khi sửa cảnh, gửi lại danh sách mới để HC thay thế cho thiết bị
- Gửi [] nếu muốn xoá trắng danh sách cảnh dưới thiết bị

### Gán cho màn hình

1. Json mẫu

```json
{
  "CMD": "ADD_SCENE_FOR_SCREEN",
  "DATA": {
    "DEVICE_ID": "",
    "SCENES": [
      {
        "SCENE_ID": "abc-cde",
        "SCENE_NAME": "123",
        "SCENE_ICON": 1
      }
    ]
  }
}
```

2. Json phản hồi

HC phản hồi lại trạng thái gán cảnh: SUCCESS hoặc FAILED

```json
{
  "CMD": "ADD_SCENE_FOR_SCREEN",
  "DATA": {
    "DEVICE_ID": "",
    "STATUS": "SUCCESS"
  }
}
```

### Xóa cảnh cho màn hình

1. Json mẫu

```json
{
  "CMD": "DEL_SCENE_FOR_SCREEN",
  "DATA": {
    "DEVICE_ID": "",
    "SCENES": [
	"abc-cde",
	"abc-cde"
    ]
  }
}
```

2. Json phản hồi

HC phản hồi lại trạng thái gán cảnh: SUCCESS hoặc FAILED

```json
{
  "CMD": "DEL_SCENE_FOR_SCREEN",
  "DATA": {
    "DEVICE_ID": "",
    "STATUS": "SUCCESS"
  }
}
```

## EVENT TRIGGER

Chuẩn hoá lại các trường của event trigger để tạo một cấu trúc thống nhất dùng cho các tính năng: Báo thức, báo ngủ, Hẹn giờ, Routine, Rule

- Bỏ trường EVENT_TRIGGER_TYPE_ID do Scene đã có bộ bản tin riêng
- Bỏ trường GROUP_ID gây khó hiểu. Mục đích ban đầu là để chỉ định ID của Rule hay Scene trên app. Đồng nhất với EVENT_TRIGGER_ID
- Bỏ trường HAS_TIMER không cần thiết. Nếu có thời gian sẽ gửi kèm START_AT và END_AT
- Nếu không dùng START_AT hoặc END_AT, set mặc định về -1
- Bỏ trường HAS_REPEATER không cần thiết. Việc lặp lại theo tuần đã được thể hiện trong trường EACH_DAY
- Chuẩn hoá các điều kiện đầu vào, đầu ra thành INPUT_DEVICES, OUTPUT_DEVICES, OUTPUT_GROUPS, OUTPUT_SCENES để phục vụ linh hoạt cho các tính năng
- Với các tính năng Routine chỉ có đầu ra là cảnh, gửi OUTPUT_SCENES với 1 ID cảnh duy nhất
- Với các tính năng Báo thức, báo ngủ, hẹn giờ, routine, gửi INPUT_DEVICES là array rỗng []
- Chuẩn hoá trường FADE_IN và FADE_OUT là số nguyên dương tính theo phút dành cho báo thức và báo ngủ, đối với các tính năng không dùng các giá trị này, set mặc định về -1
- Các OUTPUT_DEVICES và OUTPUT_GROUPS sẽ được gửi kèm tập thuộc tính.
- Bản tin Rule do có thể sử dụng tất cả các trường INPUT_DEVICES, OUTPUT_DEVICES, OUTPUT_GROUPS, OUTPUT_SCENES nên sẽ rất lớn nếu người dùng chọn nhiều. Với giới hạn 32kb cần test cụ thể để tìm được số lượng tối đa cho thiết bị đầu vào và thiết bị / nhóm / cảnh đầu ra một cách hợp lý
- Chuẩn hoá trường STATUS với 0 là DISABLED và 1 là ENABLED
- STATUS mặc định cho EVENT_TRIGGER mới là 1
- LOGICAL_OPERATOR_ID chỉ gửi kèm nếu có INPUT_DEVICES, ngược lại mặc định là -1 (Theo thời gian), 0 là OR, 1 là AND

### Cập nhật ngày 25-08

Trong phần INPUT_DEVICES / DEVICE_ATTRIBUTE:

- VALUE chuyển sang dạng array 2 giá trị [x, y] để loại bỏ COMPERATION_OPERATOR_ID.
- Đối với trường hợp dấu bằng, có thể thống nhất sử dụng giá trị đầu tiên và bỏ qua giá trị thứ 2 hoặc đặt 2 giá trị về bằng nhau.

### Tạo event trigger

1. Json mẫu

```json
{
  "CMD": "CREATE_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "PRIORITY": 1,
    "START_AT": "10:56:1",
    "END_AT": "11:09",
    "TURN_OFF_AT": "11:10",
    "FADE_IN": -1,
    "FADE_OUT": -1,
    "EACH_DAY": ["EACHMONDAY", "EACHTUESDAY"],
    "LOGICAL_OPERATOR_ID": 1,
    "STATUS": 1,
    "INPUT_DEVICES": [
      {
        "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
        "DEVICE_ATTRIBUTE": {
          "ID": 0,
          "VALUE": [0, 1]
        }
      }
    ],
    "OUTPUT_DEVICES": [
      {
        "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
        "PROPERTIES": [
          {
            "ID": 0,
            "VALUE": 1
          }
        ]
      }
    ],
    "OUTPUT_GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
        "PROPERTIES": [
          {
            "ID": 0,
            "VALUE": 1
          }
        ]
      }
    ],
    "OUTPUT_SCENES": ["aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"]
  }
}
```

2. Json phản hồi

```json
{
  "CMD": "CREATE_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": "SUCCESS"
  }
}
```

### Sửa event trigger

1. Bản tin gửi xuống

- Khi sửa event trigger, app sẽ gửi lại toàn bộ nội dung event trigger xuống. HC thay thế toàn bộ nội dung event trigger cũ bằng event trigger mới được gửi xuống từ app theo EVENT_TRIGGER_ID
- Nội dung bản tin giống với bản tin tạo, Command đổi thành EDIT_EVENT_TRIGGER

2. Bản tin phản hồi

```json
{
  "CMD": "EDIT_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": "SUCCESS"
  }
}
```

### Thay đổi trạng thái

1. Json mẫu

Thay đổi trạng thái kích hoạt của event trigger

- Command đổi thành EVENT_TRIGGER_STATUS

```json
{
  "CMD": "EVENT_TRIGGER_STATUS",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": 0
  }
}
```

2. Json phản hồi

Giống bản tin gửi đi nhưng được gửi vào topic phản hồi

### Xoá event trigger

1. Json mẫu

Xoá event trigger khỏi HC

- Command đổi thành DELETE_EVENT_TRIGGER

```json
{
  "CMD": "DELETE_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Json phản hồi

Giống bản tin gửi đi nhưng được gửi vào topic phản hồi

## HCL

### Bản tim tạo

1. Bản tin App -> HC

```json
{
  "CMD": "CREATE_HCL",
  "DATA": {
    "EVENT_TRIGGER_ID": "8967987432897",
    "EVENT_TRIGGER_TYPE_ID": 3,
    "EACH_DAY": [
      "EACHMONDAY",
      "EACHTUESDAY"
    ],
    "STATUS": 1,
    "GROUP_ID": "27866687789989",
    "STATES": [
      {
        "TIME": "8:0",
        "PROPERTIES": [
          {
            "ID": 1,
            "VALUE": 1
          },
          {
            "ID": 2,
            "VALUE": 100
          }
        ]
      },
      {
        "TIME": "10:0",
        "PROPERTIES": [
          {
            "ID": 1,
            "VALUE": 1
          },
          {
            "ID": 2,
            "VALUE": 100
          }
        ]
      },
      {
        "TIME": "12:0",
        "PROPERTIES": [
          {
            "ID": 1,
            "VALUE": 1
          },
          {
            "ID": 2,
            "VALUE": 100
          }
        ]
      }
    ]
  }
}
```

2. Bản tin HC -> APP

```json
{
  "CMD": "CREATE_HCL",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": "SUCCESS"
  }
}

```

### Bản tin sửa

1. Bản tin App -> HC

Giống bản tin tạo nhưng thay đổi CMD -> EDIT_HCL

2. Bản tin HC -> App

```json
{
  "CMD": "EDIT_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": "SUCCESS"
  }
}
```

### Bản tin xóa

1. Bản tin App -> HC

```json
{
  "CMD": "DELETE_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
  }
}
```

2. Bản tin HC -> App

```json
{
  "CMD": "DELETE_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": "SUCCESS"
  }
}
```

### Bản tin thay đổi trạng thái

1. Bản tin App -> HC

```json
{
  "CMD": "HCL_RULE_STATUS",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": 1,
    "DISABLE":[
      "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
      "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2"
      ]
  }
}
```

2. Bản tin HC -> App

```json
{
  "CMD": "HCL_RULE_STATUS",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "STATUS": "SUCCESS"
    
    
  }
}
```

## COUNTDOWN

Bản tin này dành riêng cho countdown nhằm giảm đi sự phức tạp của việc tính toán thời gian cho countdown giữa APP - HC.
APP sẽ thực hiện việc tính toán thời gian.
HC chỉ cần quan tâm thời điểm để bật cảnh và id của cảnh cần bật và tạo event trigger tương ứng

### Bản tin tạo

```json
{
  "CMD": "COUNTDOWN",
  "DATA": {
    "EVENT_TRIGGER_ID": "",
    "START_AT": "10:10",
    "SCENE_ID": "abc"
  }
}
```

### Bản tin xoá

```json
{
  "CMD": "DELETE_COUNTDOWN",
  "DATA": {
    "EVENT_TRIGGER_ID": ""
  }
}
```

## PHÒNG

### Tạo phòng

1. Bản tin gửi xuống
   APP gửi xuống bản tin tạo phòng bao gồm:

- Danh sách nhóm: Một nhóm dành cho Tất cả thiết bị trong phòng và các nhóm cho từng loại thiết bị riêng
- Danh sách cảnh mặc định cho phòng: gồm id, tên cảnh và danh sách thuộc tính theo từng nhóm đèn để HC điều khiển và tạo cảnh tương ứng

```json
{
  "CMD": "CREATE_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "DEVICE_TYPE_ID": 0,
        "NAME": "Tất cả thiết bị",
        "DEVICES": [
          "b717f8d8-6f18-43c0-ae46-69c32998f653",
          "b717f8d8-6f18-43c0-ae46-69c32998f654"
        ]
      },
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "DEVICE_TYPE_ID": 12001,
        "NAME": "Đèn LED Downlight",
        "DEVICES": [
          "b717f8d8-6f18-43c0-ae46-69c32998f653",
          "b717f8d8-6f18-43c0-ae46-69c32998f654"
        ]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "ABC",
        "SCENE_NAME": "Mùa đông",
        "GROUPS": [
          {
            "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
            "DEVICE_TYPE_ID": 12001,
            "PROPERTIES": [
              {
                "ID": 0,
                "VALUE": 1
              },
              {
                "ID": 1,
                "VALUE": 100
              }
            ]
          }
        ]
      }
    ]
  }
}
```

2. Bản tin phản hồi
   HC phản hồi lại trạng thái tạo phòng, bao gồm:

- Danh sách nhóm và các thiết bị thành công / thất bại khi gán vào nhóm
- Danh sách cảnh và các thiết bị thành công / thất bại khi gán vào cảnh

```json
{
  "CMD": "CREATE_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "GROUP_UNICAST_ID": 2,
        "SUCCESS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "FAILED": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "SCENE_UNICAST_ID": 2,
        "SUCCESS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "FAILED": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"]
      }
    ]
  }
}
```

### Thêm thiết bị

1. Bản tin gửi xuống
   Giả định: Phòng đã được tạo thành công.
   Khi thêm thiết bị vào phòng ta cần:

- Thêm đèn vào nhóm "Tất cả thiết bị" và nhóm thiết bị của riêng nó
- Nếu nhóm đèn riêng chưa tồn tại, nó sẽ được tạo mới và gán một UUID tương ứng
- Gán đèn vào danh sách cảnh mặc định

```json
{
  "CMD": "ADD_DEVICE_TO_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "GROUP_UNICAST_ID": 2,
        "DEVICE_TYPE_ID": 12001,
        "NAME": "Đèn LED Downlight",
        "DEVICES": [
          "b717f8d8-6f18-43c0-ae46-69c32998f653",
          "b717f8d8-6f18-43c0-ae46-69c32998f654"
        ]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "ABC",
        "SCENE_NAME": "Mùa đông",
        "SCENE_UNICAST_ID": 2,
        "DEVICES": [
          {
            "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
            "DEVICE_TYPE_ID": 12001,
            "PROPERTIES": [
              {
                "ID": 0,
                "VALUE": 1
              },
              {
                "ID": 1,
                "VALUE": 100
              }
            ]
          }
        ]
      }
    ]
  }
}
```

2. Bản tin phản hồi
   HC phản hồi lại trạng thái của các thiết bị theo từng nhóm / cảnh

```json
{
  "CMD": "ADD_DEVICE_TO_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "GROUP_UNICAST_ID": 2,
        "SUCCESS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "FAILED": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "SCENE_UNICAST_ID": 2,
        "SUCCESS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "FAILED": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"]
      }
    ]
  }
}
```

### Xoá thiết bị

Luồng xoá thiết bị cần được thực hiện độc lập và không đồng thời với thêm thiết bị để giảm thiểu độ phức tạp của xử lý bản tin phía HC. Trong luồng này. HC chỉ cần đảm bảo xoá các thiết bị được yêu cầu ra khỏi nhóm tương ứng của chúng (bao gồm nhóm Tất cả thiết bị) và các cảnh mặc định.

1. Bản tin gửi xuống

```json
{
  "CMD": "REMOVE_DEVICE_FROM_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "GROUP_UNICAST_ID": 2,
        "DEVICE_TYPE_ID": 12001,
        "DEVICES": [
          "b717f8d8-6f18-43c0-ae46-69c32998f653",
          "b717f8d8-6f18-43c0-ae46-69c32998f654"
        ]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f654",
        "SCENE_UNICAST_ID": 2,
        "DEVICES": ["b717f8d8-6f18-43c0-ae46-69c32998f654"]
      }
    ]
  }
}
```

2. Bản tin phản hồi

```json
{
  "CMD": "REMOVE_DEVICE_FROM_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "GROUP_UNICAST_ID": 2,
        "SUCCESS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "FAILED": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
        "SCENE_UNICAST_ID": 2,
        "SUCCESS": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"],
        "FAILED": ["aa3549d4-5471-4d75-b0b2-b70fa5c10fb2"]
      }
    ]
  }
}
```

### Xoá phòng

1. Bản tin đề xuất
   APP gửi xuống danh sách nhóm HC thực hiện kiểm tra danh sách nhóm / cảnh tương ứng với từng thiết bị và xoá các nhóm / cảnh khỏi thiết bị đó.

```json
{
  "CMD": "DELETE_ROOM",
  "DATA": {
    "GROUPS": ["b717f8d8-6f18-43c0-ae46-69c32998f653"],
    "SCENES": ["b717f8d8-6f18-43c0-ae46-69c32998f653"],
    "EVENT_TRIGGER": ["b717f8d8-6f18-43c0-ae46-69c32998f653", "b717f8d8-6f18-43c0-ae46-69c32998f653"]
  }
}
```

HC phản hồi lại trạng thái của các thiết bị được thực hiện thành công và thất bại.
CHÚ Ý: Khi xoá nhóm và cảnh, HC cần xoá tất cả các event trigger liên quan.

```json
{
  "CMD": "DELETE_ROOM",
  "DATA": {
    "GROUPS": [
      {
        "GROUP_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
        "GROUP_UNICAST_ID": 2,
        "SUCCESS": ["b717f8d8-6f18-43c0-ae46-69c32998f653"],
        "FAILED": ["b717f8d8-6f18-43c0-ae46-69c32998f653"]
      }
    ],
    "SCENES": [
      {
        "SCENE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
        "SCENE_UNICAST_ID": 2,
        "SUCCESS": ["b717f8d8-6f18-43c0-ae46-69c32998f653"],
        "FAILED": ["b717f8d8-6f18-43c0-ae46-69c32998f653"]
      }
    ],
    "EVENT_TRIGGER": [
      {
        "EVENT_TRIGGER_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
	"STATUS": "SUCCESS"	
      }
    ],
  }
}
```

### Check Room

```json
{
  "CMD" : "CHECK_ROOM",
  "DATA" : {
    "ROOM_ID" : "273a7e38-93af-4c20-8092-30db15084873"
  }
}
```

## CẤU HÌNH HC

- Reset HC: thao tác này giúp người dùng có cơ chế reset HC bằng cách gửi lệnh từ APP hoặc Cloud. Khi thực hiện reset HC cần reset tất cả các nodes và xoá toàn bộ dữ liệu thuộc về HC đó.

### Reset HC

Bản tin reset dữ liệu HC từ APP:

```json
{
  "CMD": "RESET_HC"
}
```

- Với bản tin này, HC sẽ cần thực hiện reset toàn bộ các node trong mạng và phản hồi lại trạng thái cho App biết. Sau đó, HC sẽ tự reset chính nó.
- Các thiết bị offline trong giai đoạn này sẽ cần được thực hiện reset bằng tay.
- Sau khi nhận được phản hồi, APP sẽ coi như HC đã thực hiện reset thành công và xoá dữ liệu của HC ra khỏi app.
- Nếu thao tác tự reset của HC thất bại, người dùng sẽ cần thực hiện thao tác reset cứng.

```json
{
  "CMD": "RESET_HC",
  "DATA": {
    "STATUS": "SUCCESS"
  }
}
```

### OTA HC

Bản tin App gửi cho HC khi app phát hiện ra bản cập nhật HC mới

```json
{
  "CMD": "UPDATE_FIRMWARE",
  "DATA": [
    {
      "NAME": "V1.0.2",
      "CHECK_SUM": "AFJDJE:KHJKLHALKFHJLK:JER",
      "URL": "https://jsoneditoronline.org/V1.0.2"
    },
    {
      "NAME": "V1.0.3",
      "CHECK_SUM": "AFJDJE:KHJKLHALKFHJLK:JER",
      "URL": "https://jsoneditoronline.org/V1.0.3"
    }
  ]
}
```
Khi HC gửi Version hiện tại của HC App kiêm tra Ver HC hiện tại có phải là vẻ mới chất chưa nếu chứa thì gửi lại cho HC các Ver HC mới hơn Ver hiện tại của HC

## CÁC THIẾT BỊ SMART HOME

Trong phần này, một số thiết bị cảm biến đã được mô tả trong mục BẢN TIN ĐIỀU KHIỂN - SENSOR

### Bản tin cấu hình PIN

- Đối với các thiết bị dùng PIN, ngoại trừ cảm biến khói báo PIN theo dạng pin yếu / pin đầy, các thiết bị khác sẽ báo PIN dưới dạng phần trăm
- App cần có tính năng thông báo PIN yếu: giá trị 0 đối với cảm biến khói và giá trị dưới 20 đối với các cảm biến báo dạng phần trăm
- Mã thuộc tính BATTERY là 8, xem trong bảng thuộc tính thiết bị
- Dưới đây là bản tin báo trạng thái PIN dạng phần trăm:

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 8,
        "VALUE": 1
      }
    ]
  }
}
```

### Cảm biến ánh sáng - chuyển động

#### Bản tin cấu hình

Bản tin cấu hình cho cảm biến ánh sáng đã được mô tả tại đây

- Bổ sung thêm tính năng cấu hình thời gian ACTIME độc lập cho cảm biến giống với mẫu bản tin điều khiển thiết bị:

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 17,
        "VALUE": 1
      }
    ]
  }
}
```

Với 17 là ID của thuộc tính ACTIME

#### Công tắc cảm ứng và ổ cắm

Các thiết bị này cùng có bản chất kĩ thuật chung là:

- Có các thuộc tính dạng button, với bộ ổ cắm kéo dài thì chỉ có 1 button dùng chung cho một hoặc nhiều ổ cắm đơn
- Có thể có 1 đến 4 button
- Có tính năng hẹn giờ và count down

#### Bản tin điều khiển và phản hồi trạng thái:

- Giống với bản tin điều khiển và phản hồi trạng thái thiết bị thông thường
- Các thuộc tính button: BUTTON_1 đến BUTTON_4 có ID tuần tự từ 11 đến 14 trong bảng thuộc tính thiết bị
- App dựa theo loại thiết bị (DeviceTypeId) để hiển thị số nút tương ứng hoặc trạng thái bật tắt dành cho giao diện ổ cắm riêng.
- Đối với công tắc cảm ứng, các nút được hiển thị theo thứ tự từ trái sang phải, từ trên xuống dưới.

#### Bản tin bật / tắt

Tuân theo mẫu bản tin điều khiển thiết bị thông thường:

- ID thuộc tính là mã của các nút trong bảng thuộc tính: 11 cho BUTTON_1, 12 cho BUTTON_2
- VALUE là trạng thái bật / tắt của button đó
- Bản tin phản hồi giống với bản tin gửi đi

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 11,
        "VALUE": 1
      }
    ]
  }
}
```

#### Bản tin hẹn giờ

Tính năng hẹn giờ dùng cho việc cấu hình thời gian bật / tắt dành cho công tắc hay ổ cắm theo thời điểm cụ thể trong ngày và có thể lặp lại theo ngày trong tuần.

- Sử dụng bản tin event trigger để cấu hình hẹn giờ cho công tắc / ổ cắm. Với thiết bị này là output.
- Bản tin hẹn giờ không có các điều kiện Input devices hay Output scenes, chỉ theo thời gian.
- Sử dụng trường START_AT trong event trigger cho hẹn giờ để bật / tắt ổ cắm tại giờ đã hẹn. Không có trạng thái END_AT cho trường hợp này.
- Các nhu cầu phức tạp hơn về mặt thời gian sẽ sử dụng tính năng Rule để đáp ứng.
  Ví dụ bản tin hẹn giờ bật công tắc vào 8h sáng hàng ngày:

```json
{
  "CMD": "CREATE_EVENT_TRIGGER",
  "DATA": {
    "EVENT_TRIGGER_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
    "PRIORITY": 1,
    "START_AT": "10:56:1",
    "EACH_DAY": ["EACHMONDAY", "EACHTUESDAY"],
    "STATUS": 1,
    "OUTPUT_DEVICES": [
      {
        "DEVICE_ID": "aa3549d4-5471-4d75-b0b2- b70fa5c10fb2",
        "PROPERTIES": [
          {
            "ID": 0,
            "VALUE": 1
          }
        ]
      }
    ]
  }
}
```

#### Bản tin countdown

Làm tương tự phần Countdown dành cho đèn thông thường

##### Bản tin tạo countdown

- BUTTON là thứ tự của nút. Mặc định là 1 cho ổ cắm
- Đối với hẹn giờ, app tự tính ra khoảng thời gian theo giây kể từ thời điểm hiện tại
- CHANGE_AT là thời điểm xảy ra hẹn giờ
- CHANGE_TO là trạng thái mới khi hẹn giờ xảy ra
- Một nút có thể có nhiều hẹn giờ

```json
{
  "CMD": "POWER_SWITCH_TIMEOUT",
  "DATA": {
    "EVENT_TRIGGER_ID": "",
    "DEVICE_ID": "",
    "BUTTON": 1,
    "CHANGE_AT": "2021-08-25 10:1:1",
    "CHANGE_TO": 1
  }
}
```

Phản hồi:

- STATUS: trạng thái tạo hẹn giờ phía HC: SUCCESS hoặc FAILED

```json
{
  "CMD": "POWER_SWITCH_TIMEOUT",
  "DATA": {
    "EVENT_TRIGGER_ID": "",
    "DEVICE_ID": "",
    "STATUS": "SUCCESS"
  }
}
```

##### Bản tin xoá countdown

Gửi đi:

```json
{
  "CMD": "REMOVE_POWER_SWITCH_TIMEOUT",
  "DATA": {
    "EVENT_TRIGGER_ID": ""
  }
}
```

Phản hồi:

```json
{
  "CMD": "REMOVE_POWER_SWITCH_TIMEOUT",
  "DATA": {
    "EVENT_TRIGGER_ID": "",
    "STATUS": "SUCCESS"
  }
}
```

#### Công tắc rèm cửa

Bổ sung thêm 4 thuộc tính sau dành cho rèm cửa:

|     |           |                              |       |         |
| :-- | :-------- | :--------------------------- | :---- | :------ |
| 54  | BTN_OPEN  | Nút mở rèm                   | 0, 1  | Bit     |
| 55  | BTN_CLOSE | Nút đóng rèm                 | 0, 1  | Bit     |
| 56  | BTN_PAUSE | Nút tạm dừng                 | 0, 1  | Bit     |
| 57  | OPENED    | Phần trăm giá trị mở của rèm | 1-100 | Integer |

- Mỗi nút khi được nhấn sẽ có trạng thái là bật
- Khi một nút bật thì tất cả các nút còn lại sẽ tắt
- Khi việc đóng / mở rèm kết thúc thì nút sẽ được tự động chuyển sang trạng thái tắt

##### Bản tin điều khiển

Giống với bản tin điều khiển thiết bị thông thường, với ID của các property là 54, 55, 56

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 54,
        "VALUE": 1
      }
    ]
  }
}
```

##### Bản tin phản hồi

- Bản tin phản hồi trạng thái nút sẽ được gửi vào topic phản hồi tương ứng với từng lệnh điều khiển
- Khi trạng thái mở rèm (%) thay đổi, phản hồi giá trị đó về cho app
- Khi trạng thái rèm tiến về 0 hoặc 100, trạng thái các nút cần được chuyển về tắt và việc cuộn rèm sẽ dừng lại

```json
{
  "CMD": "DEVICE",
  "DATA": {
    "DEVICE_ID": "b717f8d8-6f18-43c0-ae46-69c32998f653",
    "PROPERTIES": [
      {
        "ID": 57,
        "VALUE": 1
      }
    ]
  }
}
```

# BẢN TIN KHÁC

Đây là các bản tin đề xuất với các loại thiết bị mới: Quạt, TV, điều hoà.

## Table of contents

- ĐIỀU HOÀ
- QUẠT / TV
- IR DEVICES

## ĐIỀU HOÀ

1. Json mẫu

```json
{
  "CMD": "IR_CONTROL_AIR_CONDITION",
  "TYPE": "CONTROL",
  "DATA": {
    "IR_DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "PROPERTIES": {
      "TEMP": 16
    }
  }
}
```

Điều khiển điều hòa IR

2. Bản tin phản hồi

```json
{
  "CMD": "IR_CONTROL_AIR_CONDITION",
  "TYPE": "CONTROL",
  "DATA": {
    "IR_DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "STATUS": "SUCCESS"
  }
}
```

## QUẠT / TV

1. Json mẫu

```json
{
  "CMD": "IR_FAN_TV",
  "TYPE": "CONTROL",
  "DATA": {
    "DEVICE_ID": "abc",
    "IR_DEVICE_ID": "CDE",
    "DEVICE_ATTRIBUTE_ID": 34
  }
}
```

Điều khiển quạt/TV IR

2. Json phản hồi

```json
{
  "CMD": "IR_FAN_TV",
  "TYPE": "CONTROL",
  "DATA": {
    "DEVICE_ID": "abc",
    "IR_DEVICE_ID": "CDE",
    "STATUS": "SUCCESS"
  }
}
```

## IR DEVICES

### Điều hòa

1. Bản tin tìm chuẩn điều khiển

```json
{
  "CMD": "IR_CONTROL_AIR_CONDITION",
  "TYPE": "CHECK_CONTROL",
  "DATA": {
    "IR_DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "STANDARD_ID": 12
  }
}
```

2. Phản hồi bản tin tìm chuẩn điều khiển

```json
{
  "CMD": "IR_CONTROL_AIR_CONDITION_RESPONSE",
  "DATA": {
    "IR_DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "DEVICE_ID": "aa3549d4-5471-4d75-b0b2-b70fa5c10fb2",
    "STANDARD_ID": 12,
    "PROPERTIES": {
      "TEMP": 16,
      "MODE": 1,
      "SWING": 4,
      "FAN": 5
    }
  }
}
```

### Quạt/TV

1. Bản tin học lệnh điều khiển (quạt/TV)

```json
{
  "CMD": "IR_FAN_TV",
  "TYPE": "LEARN",
  "DATA": {
    "DEVICE_ID": "abc",
    "IR_DEVICE_ID": "CDE",
    "CATEGORY_ID": 12001,
    "DEVICE_ATTRIBUTE_ID": 34
  }
}
```

2. Bản tin phản hồi lệnh học (quạt/TV)

```json
{
  "CMD": "IR_FAN_TV",
  "TYPE": "LEARN",
  "DATA": {
    "DEVICE_ID": "abc",
    "IR_DEVICE_ID": "CDE",
    "IR_DEVICE_UNICAST_ID": 50,
    "DEVICE_ATTRIBUTE_ID": 34,
    "DEVICE_ATTRIBUTE_VALUE": 100
  }
}
```
