PKG_VERSION=2.0.4
PKG_DOWNLOAD_URL=https://github.com/u8sand/Baka-MPlayer/archive/v${PKG_VERSION}.tar.gz

pkg_prebuild_hook()
{
    # For ffmpeg, lame, xvidcore, x264, x265, libavdevice
    sudo dnf -y install --nogpg http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
}
