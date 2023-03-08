# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=goma
pkgver=0.1.0
pkgrel=1
pkgdesc='a stochastic Go engine written in python '
arch=('any')
url='https://github.com/gsobell/goma'
license=('GPL')
provides=("$pkgname")
depends=('python')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
noextract=()

package() {
     cd "$srcdir/$pkgname-$pkgver"
     sed -i /"import"/d  goma.py
     sed -i /"import"/d  engine.py
     cat board.py logic.py engine.py $pkgname.py >> $pkgname
     install -m 755 -TD "$pkgname" "$pkgdir/usr/bin/$pkgname"
     install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
     install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
