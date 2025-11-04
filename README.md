# Palindrome?

Sebuah program untuk membuat fungsi yang menentukan apakah sebuah array (list) 1-dimensi dari integer merupakan palindrom.

## 📝 Description

Program ini mengimplementasikan sebuah fungsi untuk mengecek apakah sebuah array (list) integer bersifat **palindrom**. Palindrom adalah kondisi di mana urutan elemen-elemen array tetap sama, baik dibaca dari depan ke belakang maupun dari belakang ke depan.

Sebagai contoh, `[2, 1, 3, 1, 2]` adalah palindrom, tetapi `[2, 2, 2, 5, 5]` bukan.

-----

## 🎯 Problem Statement

### Input:

  * Sebuah array (list) 1-dimensi berisi integer.

### Output:

  * Sebuah nilai boolean (`True` atau `False`).
      * `True` jika array tersebut adalah palindrom.
      * `False` jika array tersebut bukan palindrom.

### Rules:

1.  Program harus membandingkan elemen pertama dengan elemen terakhir, elemen kedua dengan elemen kedua terakhir, dan seterusnya, bergerak menuju ke tengah.
2.  Jika pada satu titik perbandingan elemen tidak sama, array tersebut bukan palindrom.
3.  Array kosong (`[]`) dianggap sebagai palindrom (`True`).
4.  Array dengan satu elemen (`[5]`) dianggap sebagai palindrom (`True`).

-----

## 💡 Examples

### Example 1 (Sample 1)

**Input:**

```
[2, 1, 3, 1, 2]
```

**Output:**

```
True
```

**Explanation:** Elemen-elemennya simetris: `2 == 2`, `1 == 1`, dan `3` berada di tengah.

### Example 2 (Sample 2)

**Input:**

```
[3, 7, 5, 6, 6, 5, 7, 3]
```

**Output:**

```
True
```

**Explanation:** Array ini simetris: `3 == 3`, `7 == 7`, `5 == 5`, dan `6 == 6`.

### Example 3 (Sample 3)

**Input:**

```
[3, 7, 5, 4, 6, 5, 7, 3]
```

**Output:**

```
False
```

**Explanation:** Pengecekan gagal di tengah. Elemen ke-4 (`4`) tidak sama dengan elemen ke-5 (`6`).

### Example 4 (Edge Case)

**Input:**

```
[]
```

**Output:**

```
True
```

**Explanation:** Array kosong secara trivial adalah palindrom.

### Example 5 (From Description)

**Input:**

```
[2, 2, 2, 5, 5]
```

**Output:**

```
False
```

**Explanation:** Elemen pertama (`2`) tidak sama dengan elemen terakhir (`5`).

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/array-palindrome-check.git
    cd array-palindrome-check
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Masukkan array dalam format list (misalnya, `[2, 1, 2]`) saat diminta untuk melihat hasilnya.
