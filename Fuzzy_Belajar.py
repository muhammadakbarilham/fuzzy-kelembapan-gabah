import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

print("SISTEM FUZZY INTENSITAS BELAJAR")

kesulitan = float(input(
    "\n1. Seberapa sulit materi yang sedang kamu pelajari? (0-100): "
))

pemahaman = float(input(
    "2. Seberapa baik kamu memahami materi yang sudah dipelajari? (0-100): "
))

nilai = float(input(
    "3. Berapa nilai hasil belajar kamu sebelumnya? (0-100): "
))

x = np.arange(0, 101, 1)

kesulitan_rendah = fuzz.trapmf(x, [0, 0, 40, 60])
kesulitan_tinggi = fuzz.trapmf(x, [40, 60, 100, 100])

pemahaman_rendah = fuzz.trapmf(x, [0, 0, 40, 60])
pemahaman_tinggi = fuzz.trapmf(x, [40, 60, 100, 100])

nilai_rendah = fuzz.trapmf(x, [0, 0, 40, 60])
nilai_tinggi = fuzz.trapmf(x, [40, 60, 100, 100])

intensitas_rendah = fuzz.trapmf(x, [0, 0, 40, 60])
intensitas_sedang = fuzz.trimf(x, [30, 50, 70])
intensitas_tinggi = fuzz.trapmf(x, [40, 60, 100, 100])

k_rendah = fuzz.interp_membership(
    x, kesulitan_rendah, kesulitan
)

k_tinggi = fuzz.interp_membership(
    x, kesulitan_tinggi, kesulitan
)

p_rendah = fuzz.interp_membership(
    x, pemahaman_rendah, pemahaman
)

p_tinggi = fuzz.interp_membership(
    x, pemahaman_tinggi, pemahaman
)

n_rendah = fuzz.interp_membership(
    x, nilai_rendah, nilai
)

n_tinggi = fuzz.interp_membership(
    x, nilai_tinggi, nilai
)

rule1 = np.fmin(
    np.fmin(k_rendah, p_tinggi),
    n_tinggi
)

rule2 = np.fmin(
    np.fmin(k_rendah, p_rendah),
    n_rendah
)

rule3 = np.fmin(
    np.fmin(k_tinggi, p_rendah),
    n_rendah
)

rule4 = np.fmin(
    np.fmin(k_tinggi, p_tinggi),
    n_tinggi
)

rule5 = np.fmin(
    np.fmin(k_rendah, p_tinggi),
    n_rendah
)

rule6 = np.fmin(
    np.fmin(k_tinggi, p_rendah),
    n_tinggi
)

rule7 = np.fmin(
    np.fmin(k_rendah, p_rendah),
    n_tinggi
)

rule8 = np.fmin(
    np.fmin(k_tinggi, p_tinggi),
    n_rendah
)

rule_rendah = np.fmax(
    rule1,
    rule4
)

rule_sedang = np.fmax(
    np.fmax(rule5, rule6),
    rule7
)

rule_tinggi = np.fmax(
    np.fmax(rule2, rule3),
    rule8
)

output_rendah = np.fmin(
    rule_rendah,
    intensitas_rendah
)

output_sedang = np.fmin(
    rule_sedang,
    intensitas_sedang
)

output_tinggi = np.fmin(
    rule_tinggi,
    intensitas_tinggi
)

agregasi = np.fmax(
    output_rendah,
    np.fmax(
        output_sedang,
        output_tinggi
    )
)

intensitas_hasil = fuzz.defuzz(
    x,
    agregasi,
    "centroid"
)

if intensitas_hasil < 40:
    kategori = "Rendah"
elif intensitas_hasil < 60:
    kategori = "Sedang"
else:
    kategori = "Tinggi"

print("\nHASIL FUZZY")

print("\nDerajat Keanggotaan:")
print("Kesulitan Rendah :", round(k_rendah, 2))
print("Kesulitan Tinggi :", round(k_tinggi, 2))
print("Pemahaman Rendah :", round(p_rendah, 2))
print("Pemahaman Tinggi :", round(p_tinggi, 2))
print("Nilai Rendah     :", round(n_rendah, 2))
print("Nilai Tinggi     :", round(n_tinggi, 2))

print("\nKekuatan Rule:")
print("Rule 1 :", round(rule1, 2))
print("Rule 2 :", round(rule2, 2))
print("Rule 3 :", round(rule3, 2))
print("Rule 4 :", round(rule4, 2))
print("Rule 5 :", round(rule5, 2))
print("Rule 6 :", round(rule6, 2))
print("Rule 7 :", round(rule7, 2))
print("Rule 8 :", round(rule8, 2))

print(f"\nINTENSITAS BELAJAR : {intensitas_hasil:.2f}")
print(f"KATEGORI           : {kategori}")

fig, axes = plt.subplots(
    1, 3,
    figsize=(15, 5)
)

fig.suptitle(
    "GRAFIK INPUT SISTEM FUZZY",
    fontsize=18,
    fontweight="bold"
)

ax1 = axes[0]

ax1.plot(
    x,
    kesulitan_rendah,
    color="#ffb6d9",
    linewidth=3,
    label="Rendah"
)

ax1.plot(
    x,
    kesulitan_tinggi,
    color="#e83e8c",
    linewidth=3,
    label="Tinggi"
)

ax1.axvline(
    kesulitan,
    color="#ad1457",
    linestyle="--",
    linewidth=2,
    label=f"Input = {kesulitan:.0f}"
)

ax1.set_title(
    "Kesulitan Materi",
    fontsize=13,
    fontweight="bold"
)

ax1.set_xlabel("Tingkat Kesulitan")
ax1.set_ylabel("Derajat Keanggotaan")
ax1.legend()
ax1.grid(alpha=0.25)


ax2 = axes[1]

ax2.plot(
    x,
    pemahaman_rendah,
    color="#ffc1df",
    linewidth=3,
    label="Rendah"
)

ax2.plot(
    x,
    pemahaman_tinggi,
    color="#d63384",
    linewidth=3,
    label="Tinggi"
)

ax2.axvline(
    pemahaman,
    color="#ad1457",
    linestyle="--",
    linewidth=2,
    label=f"Input = {pemahaman:.0f}"
)

ax2.set_title(
    "Pemahaman Materi",
    fontsize=13,
    fontweight="bold"
)

ax2.set_xlabel("Tingkat Pemahaman")
ax2.set_ylabel("Derajat Keanggotaan")
ax2.legend()
ax2.grid(alpha=0.25)


ax3 = axes[2]

ax3.plot(
    x,
    nilai_rendah,
    color="#ffb6d9",
    linewidth=3,
    label="Rendah"
)

ax3.plot(
    x,
    nilai_tinggi,
    color="#c2185b",
    linewidth=3,
    label="Tinggi"
)

ax3.axvline(
    nilai,
    color="#ad1457",
    linestyle="--",
    linewidth=2,
    label=f"Nilai = {nilai:.0f}"
)

ax3.set_title(
    "Nilai Hasil Belajar",
    fontsize=13,
    fontweight="bold"
)

ax3.set_xlabel("Nilai")
ax3.set_ylabel("Derajat Keanggotaan")
ax3.legend()
ax3.grid(alpha=0.25)

plt.tight_layout()
plt.show()


fig, ax = plt.subplots(
    figsize=(10, 6)
)

ax.plot(
    x,
    intensitas_rendah,
    color="#ffb6d9",
    linewidth=3,
    label="Intensitas Rendah"
)

ax.plot(
    x,
    intensitas_sedang,
    color="#ff69b4",
    linewidth=3,
    label="Intensitas Sedang"
)

ax.plot(
    x,
    intensitas_tinggi,
    color="#c2185b",
    linewidth=3,
    label="Intensitas Tinggi"
)

ax.fill_between(
    x,
    0,
    agregasi,
    color="#ff69b4",
    alpha=0.2,
    label="Hasil Agregasi"
)

ax.axvline(
    intensitas_hasil,
    color="#880e4f",
    linestyle="--",
    linewidth=3,
    label=f"Hasil = {intensitas_hasil:.2f}"
)

ax.set_title(
    f"OUTPUT INTENSITAS BELAJAR - {kategori.upper()}",
    fontsize=16,
    fontweight="bold"
)

ax.set_xlabel("Intensitas Belajar")
ax.set_ylabel("Derajat Keanggotaan")

ax.legend()
ax.grid(alpha=0.25)

plt.tight_layout()
plt.show()