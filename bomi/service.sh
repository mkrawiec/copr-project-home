PKG_VERSION=0.9.11
PKG_DOWNLOAD_URL=https://github.com/xylosper/bomi/archive/v${PKG_VERSION}.tar.gz

pkg_prebuild_hook()
{
    # For ffmpeg, lame, xvidcore, x264, x265, libavdevice
    sudo dnf -y install --nogpg http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
        
    # For libchardet
    sudo dnf -y copr enable mkrawiec/home
}
