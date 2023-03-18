# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=goma
pkgver=0.1.0
pkgrel=1
pkgdesc='A stochastic Go engine written in python '
arch=('any')
url='https://github.com/gsobell/goma'
license=('GPL')
provides=("$pkgname")
depends=('python')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
noextract=()
sha256sums=('b8be559f5c31d416efb01501f2389aaafd050a86da0b91bc7a60d960835467da')

package() {
     cd "$srcdir/$pkgname-$pkgver"
     sed -i /"import"/d  goma.py
     sed -i /"import"/d  engine.py
     cat board.py logic.py engine.py $pkgname.py >> $pkgname
     install -m 755 -TD "$pkgname" "$pkgdir/usr/bin/$pkgname"
     install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
     install -m 644 -TD "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
