FROM andyneff/voxel_globe:common

MAINTAINER Andrew Neff <andrew.neff@visionsystemsinc.com>

RUN apt-get update && \
    build_deps='python-dev gcc' && \
#Install packages
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ${build_deps} && \
#install python packages
    pip install uwsgi==2.0.13.1 && \
#Remove build only deps, and clean up
    DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove \
        ${build_deps} && \
    rm -r /var/lib/apt/lists/* /root/.cache

ADD uwsgi_entrypoint.bsh /

ENTRYPOINT ["/uwsgi_entrypoint.bsh"]

CMD ["uwsgi"]