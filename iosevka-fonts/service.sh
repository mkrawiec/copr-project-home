PKG_VERSION=1.9.1
PKG_DOWNLOAD_URL_1=https://github.com/be5invis/Iosevka/releases/download/v${PKG_VERSION}/01.iosevka-${PKG_VERSION}.zip
PKG_DOWNLOAD_URL_2=https://github.com/be5invis/Iosevka/releases/download/v${PKG_VERSION}/02.iosevka-term-${PKG_VERSION}.zip

pkg_service_hook()
{
    curl -Lo tmp_iosevka1.zip $PKG_DOWNLOAD_URL_1
    curl -Lo tmp_iosevka2.zip $PKG_DOWNLOAD_URL_2

    local tmp_dir=iosevka-fonts-$PKG_VERSION
    mkdir $tmp_dir
    unzip '*.zip' -d $tmp_dir

    tar -zcf $tmp_dir.tar.gz $tmp_dir

    mv $tmp_dir tmp_dir
}

