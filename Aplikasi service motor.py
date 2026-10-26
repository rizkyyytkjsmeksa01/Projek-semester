import calendar
from datetime import date, datetime

NAMA_BULAN = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember",
]


def hari_ini():
    return date.today()


def ke_tanggal(teks):
    # "2026-11-05" -> objek date
    return datetime.strptime(teks, "%Y-%m-%d").date()


def baca_input_tanggal(teks):
    """Terima format 05-11-2026 atau 05/11/2026. Hasilnya string 2026-11-05.
    Kalau formatnya salah, kembalikan None."""
    teks = teks.strip().replace("/", "-")
    try:
        d = datetime.strptime(teks, "%d-%m-%Y").date()
    except ValueError:
        return None
    return d.isoformat()


def format_tanggal(teks):
    d = ke_tanggal(teks)
    return f"{d.day} {NAMA_BULAN[d.month - 1]} {d.year}"


def selisih_hari(teks):
    # negatif berarti sudah lewat
    return (ke_tanggal(teks) - hari_ini()).days


def tambah_bulan(d, n):
    bulan = d.month - 1 + n
    tahun = d.year + bulan // 12
    bulan = bulan % 12 + 1
    # kalau tanggal 31 tapi bulan tujuan cuma 30 hari, pakai tanggal terakhir bulan itu
    hari = min(d.day, calendar.monthrange(tahun, bulan)[1])
    return date(tahun, bulan, hari)


def status_dari(teks):
    """Kembalikan (kode, label), misal ('telat', 'TELAT 3 hari')."""
    s = selisih_hari(teks)
    if s < 0:
        return "telat", f"TELAT {abs(s)} hari"
    if s == 0:
        return "segera", "HARI INI"
    if s <= 7:
        return "segera", f"{s} hari lagi"
    return "aman", f"{s} hari lagi"
