fetch('site.json') // 修改为你的 JSON 文件路径
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // 使用 response.json() 解析 JSON 数据
  })
  .then(jsonData => {
    const generatedHTML = generateHTML(jsonData); // 调用处理 JSON 数据的函数
    document.getElementById('dynamicContent').innerHTML = generatedHTML;
    triggerResizeEvent(); // 手动触发 resize 事件
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

function generateHTML(data) {
  let htmlContent = '';
  for (const key in data) {
    const classData = data[key];
    const classTitle = classData.class_name;
    const linkList = classData.link_list;

    // 生成类别开始的HTML
    htmlContent += `
      <div class="d-flex flex-fill ">
        <h4 class="text-gray text-lg mb-4">
          <i class="site-tag iconfont icon-tag icon-lg mr-1" id="term-${key.slice(-1)}"></i>
          ${classTitle}
        </h4>
        <div class="flex-fill"></div>
      </div>
    `;

    // 生成链接列表的HTML
    htmlContent += '<div class="row">';
    for (const linkKey in linkList) {
      const link = linkList[linkKey];
      // 生成单个链接的HTML
      htmlContent += `
        <div class="url-card col-6 col-sm-6 col-md-4 col-xl-5a col-xxl-6a">
          <div class="url-body default">
            <a href="${link.link}" target="_blank" data-id="${linkKey}" data-url="${link.link}" class="card no-c mb-4 site-${linkKey}" data-toggle="tooltip" data-placement="bottom" title="${link.descr}">
              <div class="card-body">
                <div class="url-content d-flex align-items-center">
                  <div class="url-img rounded-circle mr-2 d-flex align-items-center justify-content-center">
                    <img class="lazy" src="${link.img}" data-src="${link.img}" onerror="javascript:this.src='${link.img}'" alt="${link.name}">
                  </div>
                  <div class="url-info flex-fill">
                    <div class="text-sm overflowClip_1">
                      <strong>${link.name}</strong>
                    </div>
                    <p class="overflowClip_1 m-0 text-muted text-xs">${link.descr}</p>
                  </div>
                </div>
              </div>
            </a>
            <a href="${link.link}" class="togo text-center text-muted is-views" data-id="${linkKey}" data-toggle="tooltip" data-placement="right" title="直达" rel="nofollow"><i class="iconfont icon-goto"></i></a>
          </div>
        </div>
      `;
    }
    htmlContent += '</div>'; // 结束链接列表的HTML
  }

  return htmlContent;
}

function triggerResizeEvent() {
  const resizeEvent = window.document.createEvent('UIEvents');
  resizeEvent.initUIEvent('resize', true, false, window, 0);
  window.dispatchEvent(resizeEvent);
}