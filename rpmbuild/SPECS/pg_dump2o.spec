Name:           pg_dump2o
Version:        1.0
Release:        1%{?dist}
Summary:        Enhanced PostgreSQL Backup Tool

License:        MIT
URL:            https://wasiualhasib.com
Source0:        pg_dump2o

BuildArch:      noarch
Requires:       bash, tar, gzip, postgresql

%description
pg_dump2o is an enhanced PostgreSQL backup tool created by Sheikh Wasiu Al Hasib.
It supports directory and SQL backups with optional tar and gzip compression.

%prep

%build

%install
install -Dm755 %{SOURCE0} %{buildroot}/usr/local/bin/pg_dump2o

%files
/usr/local/bin/pg_dump2o

%changelog
* Thu Dec 26 2024 Sheikh Wasiu Al Hasib - 1.0-1
- Initial release
