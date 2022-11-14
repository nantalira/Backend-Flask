-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 14 Nov 2022 pada 15.27
-- Versi server: 10.4.22-MariaDB
-- Versi PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_sekolah`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('1ddccdaf469c');

-- --------------------------------------------------------

--
-- Struktur dari tabel `dosen`
--

CREATE TABLE `dosen` (
  `id` bigint(20) NOT NULL,
  `nidn` varchar(30) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `dosen`
--

INSERT INTO `dosen` (`id`, `nidn`, `nama`, `phone`, `alamat`) VALUES
(1, '123456', 'Pak Dosen', '084512354216', 'Semarang'),
(2, '654321', 'Bu Dosen', '089754213', 'Jakarta'),
(3, '456789', 'Mas Dosen', '083621456321', 'Surabaya'),
(4, '147258', 'Dedek Dosen', '021365478954', 'Balikpapan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `id` bigint(20) NOT NULL,
  `nim` varchar(30) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `phone` varchar(13) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `dosen_satu` bigint(20) DEFAULT NULL,
  `dosen_dua` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `phone`, `alamat`, `dosen_satu`, `dosen_dua`) VALUES
(2, '12712', 'Nanta', '084512354216', 'Semarang', 1, 2),
(3, '12713', 'Abu Basah', '01455796548', 'Jayapura', 2, 3),
(4, '12714', 'Slamet Riyadi', '021458796545', 'Krengseng', 3, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `siswa_node`
--

CREATE TABLE `siswa_node` (
  `id_siswa` int(11) NOT NULL,
  `nisn` varchar(11) NOT NULL,
  `nama_siswa` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `siswa_node`
--

INSERT INTO `siswa_node` (`id_siswa`, `nisn`, `nama_siswa`, `alamat`) VALUES
(1, '12712', 'Nanta', 'Semarang');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(250) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `nama` varchar(250) NOT NULL,
  `level` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `email`, `password`, `created_at`, `updated_at`, `nama`, `level`) VALUES
(1, 'email@gmail.com', 'pbkdf2:sha256:260000$1f25PsHiI3kGq5Ip$26eeae318fb15a9170813737aa934531fe564d7c4f1b9353180a24c76ae61af6', '2022-09-22 10:31:49', '2022-09-22 10:31:49', 'admin 1', 1),
(2, 'email@gmail.com', 'pbkdf2:sha256:260000$IOCrx2wj45alfEpp$aaa47fc03efa44614b421ce254a77d1f9289f78f49b45c011dc8426cd7b36821', '2022-09-22 15:50:23', '2022-09-22 15:50:23', 'admin 1', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indeks untuk tabel `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `dosen_satu` (`dosen_satu`),
  ADD KEY `dosen_dua` (`dosen_dua`);

--
-- Indeks untuk tabel `siswa_node`
--
ALTER TABLE `siswa_node`
  ADD PRIMARY KEY (`id_siswa`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `dosen`
--
ALTER TABLE `dosen`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT untuk tabel `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `siswa_node`
--
ALTER TABLE `siswa_node`
  MODIFY `id_siswa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`dosen_satu`) REFERENCES `dosen` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `mahasiswa_ibfk_2` FOREIGN KEY (`dosen_dua`) REFERENCES `dosen` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
